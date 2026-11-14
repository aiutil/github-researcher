#!/usr/bin/env python3
"""Fetch GitHub trending pages and print parsed rows. Read-only HTTP."""
import re
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def parse(h):
    arts = re.findall(r'<article class="Box-row">(.*?)</article>', h, re.S)
    out = []
    for a in arts:
        m = re.search(r'<h2[^>]*>.*?<a[^>]*href="/([^"]+)"', a, re.S)
        d = re.search(r'<p[^>]*class="col-9[^"]*"[^>]*>(.*?)</p>', a, re.S)
        lang = re.search(r'itemprop="programmingLanguage">([^<]+)<', a)
        st = re.search(r'href="/[^"]+/stargazers"[^>]*>\s*([\d,]+)', a, re.S)
        today = re.search(r'([\d,]+)\s+stars\s+today', a)
        desc = ""
        if d:
            desc = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", d.group(1))).strip()
        out.append({
            "repo": m.group(1).strip() if m else "?",
            "lang": lang.group(1).strip() if lang else "-",
            "stars": st.group(1).strip() if st else "?",
            "today": today.group(1) if today else "",
            "desc": desc[:110],
        })
    return out


if __name__ == "__main__":
    for suffix in sys.argv[1:] or ["", "?since=daily", "?since=weekly", "?since=monthly"]:
        url = "https://github.com/trending" + suffix
        print("=" * 100)
        print("URL:", url)
        try:
            rows = parse(fetch(url))
        except Exception as e:
            print("  FETCH FAILED:", e)
            continue
        print("count:", len(rows))
        for r in rows:
            print(f"  {r['stars']:>7} +{r['today']:>5}/d  {r['lang']:<14} {r['repo']:<46} {r['desc']}")
