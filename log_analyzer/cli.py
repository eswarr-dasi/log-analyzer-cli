#!/usr/bin/env python3
"""CLI entry point for the log analyzer."""

import click
import json
from datetime import datetime, timedelta
from .analyzer import LogAnalyzer
from .formatter import format_report


@click.group()
@click.option('--es-host', default='localhost', envvar='ES_HOST', help='Elasticsearch host')
@click.option('--es-port', default=9200, envvar='ES_PORT', help='Elasticsearch port')
@click.pass_context
def cli(ctx, es_host, es_port):
    """Log Analyzer CLI - Analyze logs stored in Elasticsearch."""
    ctx.ensure_object(dict)
    ctx.obj['analyzer'] = LogAnalyzer(host=es_host, port=es_port)


@cli.command()
@click.option('--index', '-i', required=True, help='Elasticsearch index pattern')
@click.option('--hours', '-h', default=24, help='Hours to look back')
@click.option('--level', '-l', default='ERROR', type=click.Choice(['DEBUG', 'INFO', 'WARN', 'ERROR']))
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'csv']), default='table')
@click.pass_context
def analyze(ctx, index, hours, level, output):
    """Analyze logs and surface error patterns."""
    analyzer = ctx.obj['analyzer']
    since = datetime.utcnow() - timedelta(hours=hours)

    click.echo(f'Analyzing {index} from last {hours} hours...')
    results = analyzer.analyze_errors(index=index, since=since, level=level)

    if output == 'json':
        click.echo(json.dumps(results, indent=2, default=str))
    else:
        click.echo(format_report(results, fmt=output))


@cli.command()
@click.option('--index', '-i', required=True, help='Elasticsearch index pattern')
@click.option('--hours', '-h', default=1, help='Hours to look back')
@click.pass_context
def anomalies(ctx, index, hours):
    """Detect anomalous spike patterns in error rates."""
    analyzer = ctx.obj['analyzer']
    since = datetime.utcnow() - timedelta(hours=hours)
    spikes = analyzer.detect_spikes(index=index, since=since)

    if not spikes:
        click.echo('No anomalies detected.')
    else:
        click.secho(f'Found {len(spikes)} anomalous periods:', fg='red')
        for spike in spikes:
            click.echo(f"  {spike['timestamp']}: {spike['count']} errors (z={spike['z_score']:.2f})")


if __name__ == '__main__':
    cli()
