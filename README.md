# GitHub Researcher

<h3 align="center">Daily, evidence-linked research on fast-moving open-source projects and developer trends.</h3>

<p align="center">
  More than a ranking table: what changed, why it may matter, how strong the signal is, and what remains unverified.
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="https://github-research.aiutil.com">Live research site</a> ·
  <a href="daily/2026-11-23.md">Latest report</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="README data checks" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 license" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="Daily research" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub Researcher live site](docs/images/readme-overview.png)

## Latest report · 2026-11-23

| Repositories analyzed today | Research archive | Core directions | Weekly star movement |
| ---: | ---: | ---: | ---: |
| 9 | 842 | 5 | 45k+ |

| Repository | Snapshot | Category |
| --- | --- | --- |
| [backnotprop/plannotator](projects/plannotator.md) | 14,399 stars | 工具型 |
| [alibaba/open-code-review](projects/alibaba-open-code-review.md) | 55,384 stars | 生产可用 |
| [elementalsouls/Claude-BugHunter](projects/claude-bughunter.md) | 17,618 stars | 工具型 |
| [affaan-m/ECC](projects/ecc.md) | 306,433 stars | 平台候选 |
| [obra/superpowers](projects/superpowers.md) | 324,102 stars | 平台候选 |
| [jingyaogong/minimind](projects/minimind.md) | 68,602 stars | 观察型 |
| [nginx/nginx](projects/nginx.md) | 32,874 stars | 基础设施候选 |
| [HKUDS/CLI-Anything](projects/cli-anything.md) | 62,725 stars | 平台候选 |

![Thirty-day GitHub research activity](docs/images/research-activity.svg)

## Current trend signals

1. **Signal 1** · score 96 · repositories: backnotprop/plannotator, alibaba/open-code-review, zhouxiaoka/autoclip
2. **Signal 2** · score 95 · repositories: affaan-m/ECC, backnotprop/plannotator, cursor/plugins
3. **Signal 3** · score 93 · repositories: elementalsouls/Claude-BugHunter, obra/superpowers, mvanhorn/last30days-skill
4. **Signal 4** · score 89 · repositories: obra/superpowers, HKUDS/CLI-Anything, backnotprop/plannotator

The structured source reports are written in Chinese today; the charts, repository snapshots, methodology, and evidence boundaries are bilingual. Follow the [latest report](daily/2026-11-23.md) for the complete source-linked reasoning record.

## Recent research cadence

| Date | Repositories analyzed | Core directions |
| --- | ---: | ---: |
| [2026-11-23](daily/2026-11-23.md) | 9 | 5 |
| [2026-11-18](daily/2026-11-18.md) | 9 | 5 |
| [2026-11-17](daily/2026-11-17.md) | 9 | 5 |
| [2026-11-16](daily/2026-11-16.md) | 9 | 5 |
| [2026-11-15](daily/2026-11-15.md) | 7 | 5 |
| [2026-11-14](daily/2026-11-14.md) | 6 | 5 |
| [2026-11-13](daily/2026-11-13.md) | 6 | 4 |

## Why this repository exists

GitHub Trending reveals attention, not durable value. This project records dated repository facts, reads the underlying code and documentation, compares multi-day movement, separates observations from inference, and keeps explicit risks such as unverifiable benchmarks or suspicious star patterns.

## Research workflow

```mermaid
flowchart LR
  A["Collect public repository signals"] --> B["Read code, docs, releases and metadata"]
  B --> C["Compare multi-day movement"]
  C --> D["Classify value and risk"]
  D --> E["Publish daily report"]
  E --> F["Update project archive and trend ledger"]
```

- `daily/` contains dated research reports with source snapshots.
- `projects/` contains durable project records and later corrections.
- `indexes/` tracks cross-project trends over time.
- `docs/` is the generated public site.
- `scripts/generate_readme.py` regenerates both READMEs and the activity chart from committed data.

## Evidence boundaries

Stars, forks, releases, licenses, languages, and timestamps are treated as observable GitHub facts at collection time. Product quality, architectural significance, market direction, and suspected manipulation are research judgments. Author claims are labeled until independently reproduced; corrections stay in the dated record.

## Generate and verify

```bash
python3 -m pip install pyyaml
python3 scripts/generate_readme.py
git diff --exit-code -- README.md README.zh-CN.md docs/images/research-activity.svg
```

The scheduled research worker runs in AIUtil's private automation environment. Tokens, private runtime memory, and operator state are not committed.

## Security

Do not add access tokens, private repository content, user-level activity, or unredacted operator memory. Report vulnerabilities privately through [GitHub Security Advisories](https://github.com/aiutil/github-researcher/security/advisories/new).

## License

Apache License 2.0. See [NOTICE](NOTICE).
