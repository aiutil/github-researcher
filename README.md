# GitHub Researcher

[简体中文](README.zh-CN.md) · [Live site](https://github-research.aiutil.com) · [AIUtil](https://aiutil.com)

GitHub Researcher follows public repository activity and turns noteworthy
changes into dated, source-linked research notes. It is intended for engineers
who need more context than a ranking table: what changed, why it may matter,
and what remains unverified.

Reports are stored in `daily/`, project records in `projects/`, and generated
site files in `docs/`.

## Build the site

```bash
python3 docs/generate_pages.py
```

The scheduled research job runs in the private AIUtil automation environment.
Credentials, private memory, and operator state are not part of this
repository.

## License

Apache License 2.0. See [NOTICE](NOTICE).
