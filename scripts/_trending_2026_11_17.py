#!/usr/bin/env python3
"""Parse GitHub trending HTML (daily/weekly) into a compact table.

Regexes tolerate both the current `tmp-pr-4` description class and the
older `pr-4` one.
"""
import html
import json
import re

ART = re.compile(r'<article class="Box-row">.*?</article>', re.S)
REPO = re.compile(r'<h2 class="h3 lh-condensed">.*?href="/([^"?]+)"', re.S)
DESC = re.compile(r'<p class="[^"]*col-9[^"]*"[^>]*>\s*(.*?)\s*</p>', re.S)
LANG = re.compile(r'<span itemprop="programmingLanguage">([^<]+)</span>')
STAR = re.compile(r'href="/[^"]+/stargazers"[^>]*>.*?</svg>\s*([\d,]+)\s*</a>', re.S)
FORK = re.compile(r'href="/[^"]+/forks"[^>]*>.*?</svg>\s*([\d,]+)\s*</a>', re.S)
TODAY = re.compile(r'([\d,]+)\s*stars?\s+(?:today|this week|this month)')


def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).strip()


def parse(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for block in ART.findall(src):
        m = REPO.search(block)
        if not m:
            continue
        repo = m.group(1)
        d = DESC.search(block)
        desc = strip_tags(d.group(1)) if d else ""
        lm = LANG.search(block)
        sm = STAR.search(block)
        fm = FORK.search(block)
        tm = TODAY.search(strip_tags(block))
        out.append({
            "repo": repo,
            "desc": desc,
            "lang": lm.group(1).strip() if lm else "",
            "stars": int(sm.group(1).replace(",", "")) if sm else None,
            "forks": int(fm.group(1).replace(",", "")) if fm else None,
            "period_stars": tm.group(1).replace(",", "") if tm else None,
        })
    return out


if __name__ == "__main__":
    res = {k: parse(f"/tmp/trend_{k}.html") for k in ("daily", "weekly")}
    json.dump(res, open("/tmp/trending.json", "w"), ensure_ascii=False, indent=1)
    for k, v in res.items():
        print(f"\n===== {k} ({len(v)}) =====")
        for r in v:
            print(f"{r['repo']:<50} *{r['stars']:<7} +{r['period_stars']:<7} "
                  f"{(r['lang'] or '-'):<13} {r['desc'][:76]}")
