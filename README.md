# GitHub Researcher

<h3 align="center">Daily, evidence-linked research on fast-moving open-source projects and developer trends.</h3>

<p align="center">
  More than a ranking table: what changed, why it may matter, how strong the signal is, and what remains unverified.
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="https://github-research.aiutil.com">Live research site</a> ·
  <a href="daily/2026-11-15.md">Latest report</a> ·
  <a href="https://aiutil.com">AIUtil</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/github-researcher/actions/workflows/ci.yml"><img alt="README data checks" src="https://img.shields.io/github/actions/workflow/status/aiutil/github-researcher/ci.yml?branch=main&style=flat-square&label=research%20data"></a>
  <a href="LICENSE"><img alt="Apache-2.0 license" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="Daily research" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![GitHub Researcher live site](docs/images/readme-overview.png)

## Latest report · 2026-11-15

| Repositories analyzed today | Research archive | Core directions | Weekly star movement |
| ---: | ---: | ---: | ---: |
| 7 | 816 | 5 | 118k+ |

| Repository | Snapshot | Category |
| --- | --- | --- |
| [brisk-thrush-husky/malware-defender-desktop](projects/malware-defender-desktop.md) | 300 stars | 观察型（反例样本） |
| [WarriorRemember/IPTV_Player_2.0](projects/iptv-player-2-0.md) | 672 stars | 观察型（反例样本） |
| [hikaku-io/hikaku-extension](projects/hikaku-extension.md) | 283 stars | 工具型 |
| [opencoredev/islandcn](projects/islandcn.md) | 658 stars | 基础设施候选 |
| [faizfahmi77/ScanDot](projects/scandot.md) | 532 stars | 工具型 |
| [quer3q/kraken-mount](projects/kraken-mount.md) | 321 stars | 工具型 |
| [duwqijlk/muse-protocol](projects/muse-protocol.md) | 513 stars | 观察型（反例样本） |

![Thirty-day GitHub research activity](docs/images/research-activity.svg)

## Current trend signals

1. **Signal 1** · score 97 · repositories: brisk-thrush-husky/malware-defender-desktop, bradburns2001/topaz-video-ai-desktop, brave-shell-07/izotope-rx-11-desktop
2. **Signal 2** · score 96 · repositories: Topkiflare74/ai--manus2.0, WarriorRemember/IPTV_Player_2.0, trackboatwrightplan/GitHub-Copilot-app
3. **Signal 3** · score 95 · repositories: DimensionRobin/rob-run-private-cheat, Crateryeexpiate/TradePilot, Beachfromgate/Wallet-Hunter
4. **Signal 4** · score 93 · repositories: hikaku-io/hikaku-extension, opencoredev/islandcn, faizfahmi77/ScanDot

The structured source reports are written in Chinese today; the charts, repository snapshots, methodology, and evidence boundaries are bilingual. Follow the [latest report](daily/2026-11-15.md) for the complete source-linked reasoning record.

## Recent research cadence

| Date | Repositories analyzed | Core directions |
| --- | ---: | ---: |
| [2026-11-15](daily/2026-11-15.md) | 7 | 5 |
| [2026-11-14](daily/2026-11-14.md) | 6 | 5 |
| [2026-11-13](daily/2026-11-13.md) | 6 | 4 |
| [2026-11-12](daily/2026-11-12.md) | 6 | 4 |
| [2026-11-11](daily/2026-11-11.md) | 2 | 2 |
| [2026-11-10](daily/2026-11-10.md) | 5 | 3 |
| [2026-11-09](daily/2026-11-09.md) | 4 | 2 |

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
