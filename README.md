# 🔍 log-analyzer-cli

> **Project 5 of 10** · [30-Day Dev Roadmap](https://github.com/eswarr-dasi/dev-project-roadmap) · Jul 3, 2026
>
> A **Python CLI tool** that ingests application log files, indexes them into Elasticsearch, and generates
> an actionable summary report — surfacing error rates, top error messages, spike detection, and slow
> endpoint patterns.
>
> ---
>
> ## ✨ Features
>
> - **Multi-format parsing** — Supports Apache/Nginx combined log format, JSON logs, and custom patterns
> - - **Elasticsearch indexing** — Bulk-indexes parsed log events for fast querying
>   - - **Error pattern detection** — Groups and ranks errors by frequency and first/last seen
>     - - **Anomaly detection** — Flags time windows with error rates > Nσ above baseline
>       - - **Slow request analysis** — Identifies endpoints with p95/p99 response times above threshold
>         - - **Summary report** — Outputs a human-readable Markdown report or JSON
>           - - **Time range filtering** — Analyze only logs within a specified window
>             - - **Dry-run mode** — Parse and report without indexing to Elasticsearch
>              
>               - ---
>
> ## 🛠️ Tech Stack
>
> | Layer | Technology |
> |-------|------------|
> | Language | Python 3.12 |
> | CLI | Click |
> | Elasticsearch | elasticsearch-py 8.x |
> | Data processing | pandas |
> | Packaging | Poetry |
> | Testing | pytest |
>
> ---
>
> ## 🚀 Usage
>
> ### Install
> ```bash
> git clone https://github.com/eswarr-dasi/log-analyzer-cli.git
> cd log-analyzer-cli
> pip install -e .
> ```
>
> ### Analyze a log file
> ```bash
> # Parse + index to Elasticsearch + print report
> log-analyzer analyze --file /var/log/app/app.log --index my-app-logs
>
> # Dry run (no indexing)
> log-analyzer analyze --file app.log --dry-run
>
> # Filter to last 2 hours
> log-analyzer analyze --file app.log --since 2h
>
> # Output as JSON
> log-analyzer analyze --file app.log --output json > report.json
> ```
>
> ### Commands
>
> | Command | Description |
> |---------|-------------|
> | `analyze` | Parse log file and generate report |
> | `index` | Index a log file to Elasticsearch only |
> | `search` | Search indexed logs (query, time range) |
> | `report` | Generate report from existing ES index |
>
> ---
>
> ## 📝 Sample Output
>
> ```
> 📊 Log Analysis Report — app.log
> 🗓️  Time range : 2026-07-03 08:00 → 2026-07-03 10:00
> 📄 Total events: 48,291
>
> ⚠️  Error Summary
>   Total errors   : 312 (0.65%)
>   ⚠️  Top errors:
>     [237x] NullPointerException in PaymentService.process()
>     [ 48x] Connection timeout to db-primary:5432
>     [ 27x] 404 /api/v1/users/{id} — user not found
>
> 🐌 Anomaly Windows
>   2026-07-03 09:14 — 09:16 : error rate spike (4.2σ above baseline)
>
> 🐢 Slow Endpoints (p95 > 500ms)
>   POST /api/v1/reconcile  — p95: 1240ms, p99: 2800ms
> ```
>
> ---
>
> ## 🧪 Testing
>
> ```bash
> pytest
> ```
>
> - Parser unit tests with fixture log files
> - - Anomaly detection algorithm tests
>   - - CLI command integration tests (mocked ES)
>    
>     - ---
>
> ## 🎯 Career Relevance
>
> Extends my professional Splunk and Grafana observability experience into an open-source, portable tool.
> Demonstrates Python, Elasticsearch, and data analysis skills — all highly valued for senior backend and
> platform/DevOps engineering roles.
>
> ---
>
> ## 📅 Part of the 30-Day Dev Challenge
>
> See the full roadmap: [dev-project-roadmap](https://github.com/eswarr-dasi/dev-project-roadmap)
>
> *Built by [Eswarr Dasi](https://github.com/eswarr-dasi) · Jul 2026*
