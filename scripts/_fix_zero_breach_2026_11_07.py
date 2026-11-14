#!/usr/bin/env python3
"""Fix the stale zero-breach-toolkit link and refresh the tracked zero-breach profile."""
import re

BASE = '/home/lohasle/aiutil-github-researcher/'

# --- 1. daily/2026-10-30.md: name + href ---
p = BASE + 'daily/2026-10-30.md'
s = open(p, encoding='utf-8').read()
before = s
s = s.replace('  - name: interplains/Zero-Breach-Toolkit\n',
              '  - name: interplains/zero-breach\n')
s = s.replace('    href: "projects/zero-breach-toolkit.html"\n',
              '    href: "projects/zero-breach.html"\n')
s = s.replace('      - zero-breach-toolkit\n', '      - zero-breach\n')
assert s != before, 'daily 2026-10-30 unchanged'
open(p, 'w', encoding='utf-8').write(s)
print('daily/2026-10-30.md: name+href+tag fixed')
print('  remaining "zero-breach-toolkit" occurrences:', s.count('zero-breach-toolkit'))

# --- 2. projects/zero-breach.md: refresh stars + add recent activity ---
p = BASE + 'projects/zero-breach.md'
s = open(p, encoding='utf-8').read()
before = s
s = s.replace('stars: "402 stars"', 'stars: "4,475 stars"')
s = s.replace('stars_delta: "2 天 402⭐"',
              'stars_delta: "⭐ 2026-10-20 建档时 402⭐ → 2026-11-06 快照 4,475⭐（17 天 +1,011%，fork 473 / subs 42 / oi 7 · Apache-2.0 · Python · 12,477 KB）；'
              '**⭐⭐ 仓库已由 `interplains/Zero-Breach-Toolkit` 改名为 `interplains/zero-breach`（GitHub 会重定向旧路径），'
              '本日报据此把 2026-10-30 日报里指向 `projects/zero-breach-toolkit.html` 的坏链接改为 `projects/zero-breach.html`**；'
              '**⭐⭐⭐ 这也是本日报记录的第二个「改名时间戳」案例 —— 与 `mirkobrombin/raven` 同类：**若不查旧名，会把一个持续了 17 天的项目误判为「11-06 突然出现」"')
s = s.replace('last_seen_date: "2026-10-20"', 'last_seen_date: "2026-11-07"')
assert s != before, 'projects/zero-breach.md unchanged'
open(p, 'w', encoding='utf-8').write(s)
print('projects/zero-breach.md: stars + stars_delta + last_seen_date updated')
