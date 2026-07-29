#!/usr/bin/env python3
"""
GitHub Pages HTML Generator
Reads Markdown files with YAML frontmatter and generates static HTML pages.
"""

import os
import re
import glob
import yaml
import markdown
from datetime import datetime

# === Paths ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
DAILY_DIR = os.path.join(BASE_DIR, 'daily')
PROJECTS_DIR = os.path.join(BASE_DIR, 'projects')
INDEXES_DIR = os.path.join(BASE_DIR, 'indexes')

# === CSS: external stylesheet (GitHub Primer design system) ===
# All shared styles live in docs/assets/style.css, served at /assets/style.css
CSS = '    <link rel="stylesheet" href="/assets/style.css">'

NAV = '''    <nav class="nav">
        <div class="nav-inner">
            <a href="/index.html" class="nav-brand">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.09.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>
                GitHub 趋势研究
            </a>
            <div class="nav-links">
                <a href="/index.html" id="nav-home"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg><span>首页</span></a>
                <a href="/daily.html" id="nav-daily"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg><span>日报</span></a>
                <a href="/projects.html" id="nav-projects"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg><span>项目</span></a>
                <a href="/trends.html" id="nav-trends"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg><span>趋势</span></a>
            </div>
        </div>
    </nav>'''

MERMAID_SCRIPT = '''    <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true,theme:'neutral',securityLevel:'loose'});</script>'''

FOOTER = '''    <footer class="footer">
        <p><strong>AIUtil 产品</strong> · 研究内容由定时任务生成，结论以原始来源为准。</p>
        <p style="margin-top:8px;"><a href="https://aiutil.com">AIUtil</a> · <a href="https://aiutil.com/about">关于</a> · <a href="https://agentos.aiutil.com">Agent OS</a> · <a href="https://radar.aiutil.com">前沿论文</a> · <a href="https://github-research.aiutil.com">GitHub 趋势</a> · <a href="https://nimbus.aiutil.com">Nimbus</a> · <a href="https://visionai.aiutil.com">VisionAI</a> · <a href="https://github.com/aiutil/github-researcher">源码</a></p>
    </footer>'''

# Filter bar styles now live in the external stylesheet (style.css .filter-bar / .filter-group)
FILTER_CSS = ''

PROJECT_FILTER_JS = '''    <script>
    (function() {
        var grid = document.getElementById('project-grid');
        var cards = grid.querySelectorAll('.card');
        var filterLang = document.getElementById('filter-language');
        var filterCat = document.getElementById('filter-category');
        var sortBy = document.getElementById('sort-by');
        var searchInput = document.getElementById('filter-search');
        var countLabel = document.getElementById('filter-count');
        var emptyMsg = document.getElementById('filter-empty');

        function applyFilters() {
            var lang = filterLang.value;
            var cat = filterCat.value;
            var sort = sortBy.value;
            var search = (searchInput.value || '').toLowerCase().trim();
            var visible = 0;
            var cardArray = Array.from(cards);

            // Filter
            cardArray.forEach(function(c) {
                var cLang = c.getAttribute('data-language') || '';
                var cCat = c.getAttribute('data-category') || '';
                var cName = (c.getAttribute('data-name') || '').toLowerCase();
                var cDesc = (c.querySelector('.card-desc') || {}).textContent || '';
                cDesc = cDesc.toLowerCase();

                var langOk = !lang || cLang === lang;
                var catOk = !cat || cCat.indexOf(cat) >= 0;
                var searchOk = !search || cName.indexOf(search) >= 0 || cDesc.indexOf(search) >= 0;

                if (langOk && catOk && searchOk) {
                    c.style.display = '';
                    visible++;
                } else {
                    c.style.display = 'none';
                }
            });

            // Sort
            cardArray.sort(function(a, b) {
                if (sort === 'stars-desc') return (parseInt(b.getAttribute('data-stars'))||0) - (parseInt(a.getAttribute('data-stars'))||0);
                if (sort === 'stars-asc') return (parseInt(a.getAttribute('data-stars'))||0) - (parseInt(b.getAttribute('data-stars'))||0);
                if (sort === 'date-asc') return (a.getAttribute('data-date')||'').localeCompare(b.getAttribute('data-date')||'');
                if (sort === 'date-desc') return (b.getAttribute('data-date')||'').localeCompare(a.getAttribute('data-date')||'');
                if (sort === 'name') return (a.getAttribute('data-name')||'').localeCompare(b.getAttribute('data-name')||'');
                return 0;
            });

            // Re-append in sorted order
            cardArray.forEach(function(c) { grid.appendChild(c); });

            countLabel.textContent = '显示 ' + visible + ' / ' + cards.length + ' 个项目';
            emptyMsg.style.display = visible === 0 ? 'block' : 'none';
        }

        filterLang.addEventListener('change', applyFilters);
        filterCat.addEventListener('change', applyFilters);
        sortBy.addEventListener('change', applyFilters);
        searchInput.addEventListener('input', applyFilters);
        applyFilters();
    })();
    </script>'''

DAILY_FILTER_JS = '''    <script>
    (function() {
        var tbody = document.querySelector('.daily-table tbody');
        var rows = tbody.querySelectorAll('tr');
        var searchInput = document.getElementById('daily-search');
        var sortBy = document.getElementById('daily-sort');
        var countLabel = document.getElementById('daily-count');

        function applyFilters() {
            var search = (searchInput.value || '').toLowerCase().trim();
            var sort = sortBy.value;
            var visible = 0;
            var rowArray = Array.from(rows);

            rowArray.forEach(function(r) {
                var text = (r.textContent || '').toLowerCase();
                if (!search || text.indexOf(search) >= 0) { r.style.display = ''; visible++; }
                else { r.style.display = 'none'; }
            });

            if (sort === 'date-desc') rowArray.sort(function(a,b) { return (b.getAttribute('data-date')||'').localeCompare(a.getAttribute('data-date')||''); });
            else if (sort === 'date-asc') rowArray.sort(function(a,b) { return (a.getAttribute('data-date')||'').localeCompare(b.getAttribute('data-date')||''); });

            rowArray.forEach(function(r) { tbody.appendChild(r); });
            countLabel.textContent = '显示 ' + visible + ' / ' + rows.length + ' 篇日报';
        }
        searchInput.addEventListener('input', applyFilters);
        sortBy.addEventListener('change', applyFilters);
        applyFilters();
    })();
    </script>'''

TRENDS_FILTER_JS = '''    <script>
    (function() {
        var sections = document.querySelectorAll('.date-section');
        var searchInput = document.getElementById('trends-search');
        var countLabel = document.getElementById('trends-count');
        var total = sections.length;

        searchInput.addEventListener('input', function() {
            var search = (this.value || '').toLowerCase().trim();
            var visible = 0;
            sections.forEach(function(s) {
                var text = (s.textContent || '').toLowerCase();
                if (!search || text.indexOf(search) >= 0) { s.style.display = ''; visible++; }
                else { s.style.display = 'none'; }
            });
            countLabel.textContent = '显示 ' + visible + ' / ' + total + ' 天';
        });
    })();
    </script>'''


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        fm = {}

    return fm, parts[2]


def render_markdown_with_mermaid(body):
    """Render markdown, preserving mermaid code blocks as <pre class='mermaid'>."""
    # Replace ```mermaid ... ``` blocks with <pre class="mermaid"> placeholders
    # to prevent markdown from escaping them
    import hashlib
    placeholders = {}
    
    def replace_mermaid(match):
        code = match.group(1)
        key = f'MERMAID_PLACEHOLDER_{hashlib.md5(code.encode()).hexdigest()}'
        placeholders[key] = f'<pre class="mermaid">{code}</pre>'
        return key
    
    processed = re.sub(r'```mermaid\n(.*?)```', replace_mermaid, body, flags=re.DOTALL)
    html = markdown.markdown(processed, extensions=['tables', 'toc'])
    
    for key, value in placeholders.items():
        html = html.replace(f'<p>{key}</p>', value)
        html = html.replace(key, value)
    
    return html


def get_fm(fm, key, default):
    """Safely get value from frontmatter with default."""
    val = fm.get(key, default)
    return val if val is not None else default


def tag_class(tag):
    """Return CSS class for tag."""
    tag_lower = tag.lower()
    if '基础设施' in tag or 'poc' in tag_lower: return 'tag-green'
    if 'mcp' in tag_lower: return 'tag-cyan'
    if '平台' in tag: return 'tag-cyan'
    if '泡沫' in tag: return 'tag-orange'
    return 'tag-purple'


# === Generate index.html ===
def generate_index():
    # Read latest daily
    daily_files = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True)

    latest_daily_fm = {}
    latest_daily_content = ''
    if daily_files:
        with open(daily_files[0], 'r') as f:
            content = f.read()
        latest_daily_fm, latest_daily_content = parse_frontmatter(content)

    # Read all projects for key_projects
    project_files = sorted(glob.glob(os.path.join(PROJECTS_DIR, '*.md')))
    all_projects = []
    for pf in project_files:
        with open(pf, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        if fm:
            fm['href'] = fm.get('href', f"projects/{os.path.basename(pf).replace('.md', '.html')}")
            all_projects.append(fm)

    # Use frontmatter data or provide defaults
    title = get_fm(latest_daily_fm, 'title', 'GitHub 趋势研究')
    summary = get_fm(latest_daily_fm, 'summary', '持续跟踪 GitHub 热门项目与开源趋势')
    hero_badge = get_fm(latest_daily_fm, 'hero_badge', '持续更新中')
    date_str = get_fm(latest_daily_fm, 'date', datetime.now().strftime('%Y-%m-%d'))

    # === Dynamic stats: always compute from actual data ===
    # Use aggregate_all_projects() for consistency with projects page
    aggregated = aggregate_all_projects()
    real_project_count = len(aggregated)

    # Count daily reports (daily/*.md)
    daily_files_for_stats = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')))
    real_daily_count = len(daily_files_for_stats)

    # Count unique trend directions across all dailies
    unique_directions = set()
    for df in daily_files_for_stats:
        with open(df, 'r') as fp:
            c = fp.read()
        fm_d, _ = parse_frontmatter(c)
        for t in (fm_d.get('trends') or []):
            if t.get('name'):
                unique_directions.add(t['name'])
    real_directions_count = len(unique_directions)

    # Sum weekly stars from latest daily's weekly_stars field (keep as-is if string)
    weekly_stars = get_fm(latest_daily_fm, 'stats', {}).get('weekly_stars', 'N/A')

    # Override stats with real computed values (ignores frontmatter project_count)
    stats = {
        'project_count': real_project_count,
        'daily_updates': real_daily_count,
        'core_directions': real_directions_count,
        'weekly_stars': weekly_stars
    }

    trends = get_fm(latest_daily_fm, 'trends', [
        {'rank': 1, 'name': 'Multi-Agent Orchestration', 'projects': ['hermes-agent'], 'score': 60},
        {'rank': 2, 'name': 'MCP 协议扩散', 'projects': ['GitNexus', 'qmd'], 'score': 58},
    ])

    key_projects = get_fm(latest_daily_fm, 'key_projects', all_projects[:3])

    # Format weekly_stars: if numeric, convert 1234567 → "1.2M"; keep string as-is
    def fmt_num(v):
        if isinstance(v, (int, float)):
            v = int(v)
            if v >= 1_000_000:
                return f"{v/1_000_000:.2f}M".rstrip('0').rstrip('.') + '+'
            if v >= 1_000:
                return f"{v/1_000:.1f}K".rstrip('0').rstrip('.') + '+'
            return f"{v:,}+"
        return v

    weekly_stars_fmt = fmt_num(weekly_stars)

    # Stats HTML — first card highlighted as primary (hero stat)
    def stat_card(icon_path, num, label, primary=False):
        cls = "stat-card stat-card-primary" if primary else "stat-card"
        return f'''
            <div class="{cls}">
                <svg class="stat-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon_path}</svg>
                <div class="stat-number">{num}</div>
                <div class="stat-label">{label}</div>
            </div>'''

    stats_html = (
        stat_card('<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>', weekly_stars_fmt, '本周总 Star 增速', primary=True)
        + stat_card('<path d="M3 3h18v18H3z"/><path d="M3 9h18"/><path d="M9 21V9"/>', stats['project_count'], '深度分析项目')
        + stat_card('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>', stats['daily_updates'], '日更日报')
        + stat_card('<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>', stats['core_directions'], '核心跟踪方向')
    )

    # Brief card
    brief_date = f"📅 {date_str} · 今日核心判断"
    brief_title = summary
    # Dynamic brief_text from latest daily
    trends_latest = get_fm(latest_daily_fm, 'trends', [])
    top_trend = trends_latest[0]['name'] if trends_latest else summary
    brief_text = summary + (f" 今日头条趋势:{top_trend}。" if trends_latest else "")

    daily_date_filename = f"daily/{os.path.basename(daily_files[0]).replace('.md', '.html')}" if daily_files else 'daily/2026-04-07.html'

    # Key projects cards
    project_cards = ''
    for p in key_projects[:3]:
        name = p.get('title', p.get('name', 'Unknown'))
        emoji = p.get('emoji', '📦')
        stars = p.get('stars', p.get('stars_per_day', 'N/A'))
        if isinstance(stars, int):
            stars = f"{stars:,} stars/day"
        desc = p.get('desc', p.get('summary', ''))
        category = p.get('category', '')
        tags = p.get('tags', [category]) if isinstance(p.get('tags'), list) else [category]
        score = p.get('score', 'N/A')
        href = p.get('href', f"projects/{make_slug(name)}.html")
        tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags[:3]])
        # Find GitHub URL from project data
        github_url = None
        for p_all in all_projects:
            p_all_name = p_all.get('name', p_all.get('title', ''))
            if p_all_name == name or make_slug(p_all_name) == make_slug(name):
                github_url = p_all.get('url', p_all.get('github_url', None))
                break
        github_btn = ''
        if github_url:
            github_btn = f'<a href="{github_url}" target="_blank" rel="noopener" class="btn-github" onclick="event.stopPropagation();"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.09.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>GitHub</a>'
        project_cards += f'''
                <div class="card" onclick="window.location='/{href}'" style="cursor:pointer">
                    <div class="card-top">
                        <div class="card-emoji">{emoji}</div>
                        <div class="card-stars">{stars}</div>
                    </div>
                    <div class="card-title">{name}</div>
                    <div class="card-desc">{desc}</div>
                    <div class="card-tags">{tag_html}</div>
                    <div class="card-actions">{github_btn}</div>
                </div>'''

    # Trend list
    trend_rows = ''
    for t in trends[:4]:
        rank = t.get('rank', 0)
        name = t.get('name', 'Unknown')
        projects = t.get('projects', [])
        score_val = t.get('score', 0)
        is_high = score_val >= 55 if isinstance(score_val, int) else False
        rank_class = 'top' if rank <= 2 else ''
        score_class = 'high' if is_high else ''
        projects_str = ' · '.join(str(p) for p in projects[:3])
        trend_rows += f'''
                <div class="trend-item">
                    <div class="trend-rank {rank_class}">{rank}</div>
                    <div class="trend-content">
                        <div class="trend-title">{name}</div>
                        <div class="trend-meta">{projects_str}</div>
                    </div>
                    <div class="trend-score {score_class}">{score_val}/80</div>
                </div>'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GitHub Researcher</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📊</text></svg>">
    <meta name="description" content="{summary}">
{CSS}
</head>
<body>
{NAV}
<main class="container">
        <section class="hero">
            <div class="hero-meta">
                <span class="hero-meta-dot"></span>
                <span class="hero-meta-date">{date_str}</span>
                <span class="hero-meta-sep">·</span>
                <span class="hero-meta-status">{hero_badge}</span>
            </div>
            <h1 class="hero-title">GitHub 趋势研究</h1>
            <p class="hero-subtitle">每日从 GitHub Trending 中筛选真正值得架构师关注的项目——不只是搬运 star 数，而是判断它属于玩具、工具、平台还是未来基础设施。</p>
            <div class="hero-actions">
                <a href="/{daily_date_filename}" class="btn-dark">
                    阅读今日简报
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><polyline points="12 5 19 12 12 19"/></svg>
                </a>
                <a href="/projects.html" class="btn-outline">
                    浏览项目库
                </a>
            </div>
        </section>
        <section class="stats-row">{stats_html}
        </section>
        <section class="brief-card">
            <div class="brief-date">{brief_date}</div>
            <h2 class="brief-title">{brief_title}</h2>
            <p class="brief-text">{brief_text}</p>
            <a href="/{daily_date_filename}" class="brief-cta">阅读完整简报 →</a>
        </section>
        <section>
            <div class="section-header">
                <div class="section-title">
                    <span class="icon">⭐</span>
                    重点跟踪项目
                </div>
                <a href="/projects.html" class="section-link">查看全部 →</a>
            </div>
            <div class="card-grid">{project_cards}
            </div>
        </section>
        <section>
            <div class="section-header">
                <div class="section-title">
                    <span class="icon">📈</span>
                    趋势热榜
                </div>
                <a href="/trends.html" class="section-link">完整趋势表 →</a>
            </div>
            <div class="trend-list">{trend_rows}
            </div>
        </section>
        <section>
            <div class="section-header">
                <div class="section-title">
                    <span class="icon">🏷️</span>
                    核心关注领域
                </div>
            </div>
            <div class="category-row">
                <a href="/projects.html" class="category-pill"><span class="emoji">🤖</span> AI Agent / Multi-Agent</a>
                <a href="/projects.html" class="category-pill"><span class="emoji">⚡</span> LLM Infra / MCP / AI Runtime</a>
                <a href="/projects.html" class="category-pill"><span class="emoji">🛠️</span> 开发工具链 / IDE / Copilot</a>
                <a href="/projects.html" class="category-pill"><span class="emoji">🌐</span> 前端框架 / Serverless / Edge</a>
                <a href="/projects.html" class="category-pill"><span class="emoji">☸️</span> 云原生 / K8s / Service Mesh</a>
                <a href="/projects.html" class="category-pill"><span class="emoji">🔄</span> 自动化 / Browser Use / RPA+AI</a>
                <a href="/projects.html" class="category-pill"><span class="emoji">💾</span> 数据基础设施 / RAG / 向量 DB</a>
                <a href="/projects.html" class="category-pill"><span class="emoji">🔌</span> 基础设施标准 / 平台潜力</a>
            </div>
        </section>
</main>
{FOOTER}
</body>
</html>'''

    os.makedirs(DOCS_DIR, exist_ok=True)
    with open(os.path.join(DOCS_DIR, 'index.html'), 'w') as f:
        f.write(html)
    print(f"Generated index.html")


# === Generate daily listing ===
def generate_daily_list():
    daily_files = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True)

    rows = ''
    for f in daily_files:
        date = os.path.basename(f).replace('.md', '')
        with open(f, 'r') as fp:
            content = fp.read()
        fm, _ = parse_frontmatter(content)
        title = fm.get('title', f'{date} 日报')
        summary = fm.get('summary', '')
        # Extract first line of summary
        topic = summary.split('。')[0] if summary else date

        rows += f'''        <tr data-date="{date}">
            <td style="font-family:var(--font-mono);font-weight:600;">{date}</td>
            <td>{topic}</td>
            <td><a href="/daily/{date}.html" class="section-link">查看 →</a></td>
        </tr>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>日报索引 | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📊</text></svg>">
{CSS}
{FILTER_CSS}
</head>
<body>
{NAV.replace('id="nav-daily"', 'id="nav-daily" class="active"')}
<script>document.getElementById('nav-daily').classList.add('active');</script>
<main class="container">
    <div class="page-header">
        <h1>📅 日报索引</h1>
        <p>每日 GitHub 趋势研究简报,持续跟踪不间断</p>
    </div>
    <div class="filter-bar">
        <div class="filter-group">
            <label>🔍 搜索</label>
            <input type="text" id="daily-search" placeholder="搜索日期或主题...">
        </div>
        <div class="filter-group">
            <label>↕️ 排序</label>
            <select id="daily-sort">
                <option value="date-desc">日期 ↓ (新→旧)</option>
                <option value="date-asc">日期 ↑ (旧→新)</option>
            </select>
        </div>
        <span class="filter-count" id="daily-count"></span>
    </div>
    <div class="gh-table">
        <table>
            <thead>
                <tr>
                    <th>日期</th>
                    <th>核心主题</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
{rows}
            </tbody>
        </table>
    </div>
</main>
{FOOTER}
{DAILY_FILTER_JS}
</body>
</html>'''

    with open(os.path.join(DOCS_DIR, 'daily.html'), 'w') as f:
        f.write(html)
    print(f"Generated daily.html with {len(daily_files)} entries")


# === Generate individual daily page ===
def generate_daily_page(filepath):
    date = os.path.basename(filepath).replace('.md', '')

    with open(filepath, 'r') as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    html_body = render_markdown_with_mermaid(body)

    title = fm.get('title', f'{date} 日报')

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📅</text></svg>">
{CSS}
</head>
<body>
{NAV.replace('id="nav-daily"', 'id="nav-daily" class="active"')}
<main class="container">
    <a href="/daily.html" class="back-link">← 返回日报索引</a>
    <div class="content-card">
        {html_body}
    </div>
</main>
{FOOTER}
{MERMAID_SCRIPT}
</body>
</html>'''

    daily_html_dir = os.path.join(DOCS_DIR, 'daily')
    os.makedirs(daily_html_dir, exist_ok=True)
    with open(os.path.join(daily_html_dir, f'{date}.html'), 'w') as f:
        f.write(html)
    print(f"Generated daily/{date}.html")


# === Aggregate all projects from daily + projects dir ===
def aggregate_all_projects():
    """Merge projects from daily key_projects + projects/*.md, dedup by name."""
    merged = {}  # name -> project dict
    merged_by_slug = {}  # slug -> project dict

    # 1. Read projects/*.md for detailed profiles
    for pf in sorted(glob.glob(os.path.join(PROJECTS_DIR, '*.md'))):
        with open(pf, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        if not fm:
            continue
        key = fm.get('name', fm.get('title', os.path.basename(pf).replace('.md', '')))
        fm['_has_profile'] = True
        fm['_profile_slug'] = make_slug(key)
        merged[key] = fm
        # Also register by slug for cross-matching
        merged_by_slug[fm['_profile_slug']] = fm

    # 2. Walk daily/*.md newest-first, merge key_projects
    for df in sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True):
        date_str = os.path.basename(df).replace('.md', '')
        with open(df, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        kp_list = fm.get('key_projects', []) or []
        for p in kp_list:
            key = p.get('name', '')
            if not key:
                continue
            daily_slug = make_slug(key)
            # Try to match with existing profile by name or slug
            matched = merged.get(key) or merged_by_slug.get(daily_slug)
            if matched:
                for k, v in p.items():
                    if v is not None and k not in ('_has_profile', '_profile_slug'):
                        matched[k] = v
                matched['last_seen_date'] = date_str
                # Ensure the daily key also points to the same profile
                merged[key] = matched
            else:
                p = dict(p)
                p['last_seen_date'] = date_str
                merged[key] = p
            if 'first_seen_date' not in merged[key]:
                merged[key]['first_seen_date'] = date_str

    # Dedup: merged dict may contain same object under different keys
    seen = set()
    result = []
    for p in merged.values():
        pid = id(p)
        if pid not in seen:
            seen.add(pid)
            result.append(p)
    return result


# === Generate projects listing ===
def generate_projects_list():
    all_projects = aggregate_all_projects()
    # Sort by last_seen_date desc
    all_projects.sort(key=lambda p: p.get('last_seen_date', ''), reverse=True)

    # Collect unique languages and categories for filter options
    languages_set = set()
    categories_set = set()
    for p in all_projects:
        lang = p.get('language', '')
        if lang:
            languages_set.add(lang)
        cat = p.get('category', '') or p.get('verdict', '')
        if cat:
            categories_set.add(cat)

    languages = sorted(languages_set)
    categories = sorted(categories_set)

    lang_options = ''.join([f'<option value="{l}">{l}</option>' for l in languages])
    cat_options = ''.join([f'<option value="{c}">{c}</option>' for c in categories])

    cards = ''
    for p in all_projects:
        name = p.get('title', p.get('name', 'Unknown'))
        emoji = p.get('emoji', '📦')
        stars_raw = p.get('stars', p.get('stars_delta', p.get('stars_per_day', 0)))
        # Extract numeric stars for sorting
        stars_num = 0
        if isinstance(stars_raw, int):
            stars_num = stars_raw
        elif isinstance(stars_raw, str):
            m = re.search(r'[\d,]+', stars_raw)
            if m:
                stars_num = int(m.group().replace(',', ''))
        if isinstance(stars_raw, int):
            stars_display = f"{stars_raw:,} stars/day"
        else:
            stars_display = stars_raw if stars_raw else 'N/A'
        desc = (p.get('desc', p.get('description', '')) or '')[:120]
        language = p.get('language', '')
        verdict = p.get('verdict', '')
        last_seen = p.get('last_seen_date', '')
        has_profile = p.get('_has_profile', False)

        # Build tags from language + verdict + category
        tags = []
        if language:
            tags.append(language)
        if verdict and '⭐' in verdict:
            tags.append('重点跟踪')
        category = p.get('category', '')
        if category:
            tags.append(category)
        if not tags:
            tags = ['项目']

        # Build href: link to profile page if exists, else to the daily page where last seen
        if has_profile:
            slug = make_slug(name)
            href = f"projects/{slug}.html"
        else:
            href = f"daily/{last_seen}.html"

        tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags[:3]])
        seen_html = f'<div style="font-size:12px;color:var(--fg-muted);margin-top:4px;">最近出现: {last_seen}</div>' if last_seen else ''

        # GitHub URL button
        github_url = p.get('url', p.get('github_url', None))
        github_btn = ''
        if github_url:
            github_btn = f'<a href="{github_url}" target="_blank" rel="noopener" class="btn-github" onclick="event.stopPropagation();"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.09.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>GitHub</a>'

        cat_attr = category or verdict or ''
        cards += f'''                <div class="card" onclick="window.location='/{href}'" style="cursor:pointer" data-language="{language}" data-category="{cat_attr}" data-stars="{stars_num}" data-date="{last_seen}" data-name="{name}">
                    <div class="card-top">
                        <div class="card-emoji">{emoji}</div>
                        <div class="card-stars">{stars_display}</div>
                    </div>
                    <div class="card-title">{name}</div>
                    <div class="card-desc">{desc}</div>
                    <div class="card-tags">{tag_html}</div>
                    <div class="card-actions">{github_btn}</div>
                    {seen_html}
                </div>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>重点项目 | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>⭐</text></svg>">
{CSS}
{FILTER_CSS}
</head>
<body>
{NAV.replace('id="nav-projects"', 'id="nav-projects" class="active"')}
<main class="container">
    <div class="page-header">
        <h1>⭐ 重点项目</h1>
        <p>聚合自所有日报的深度分析项目,持续跟踪</p>
    </div>
    <div class="filter-bar">
        <div class="filter-group">
            <label>🔤 语言</label>
            <select id="filter-language"><option value="">全部</option>{lang_options}</select>
        </div>
        <div class="filter-group">
            <label>🏷️ 类型</label>
            <select id="filter-category"><option value="">全部</option>{cat_options}</select>
        </div>
        <div class="filter-group">
            <label>🔍 搜索</label>
            <input type="text" id="filter-search" placeholder="项目名称或描述...">
        </div>
        <div class="filter-group">
            <label>↕️ 排序</label>
            <select id="sort-by">
                <option value="date-desc">最近出现 ↓</option>
                <option value="date-asc">最近出现 ↑</option>
                <option value="stars-desc">Stars ↓</option>
                <option value="stars-asc">Stars ↑</option>
                <option value="name">名称 A-Z</option>
            </select>
        </div>
        <span class="filter-count" id="filter-count"></span>
    </div>
    <div class="filter-empty" id="filter-empty">😢 没有匹配的项目</div>
    <div class="card-grid" id="project-grid">
{cards}
    </div>
</main>
{FOOTER}
{PROJECT_FILTER_JS}
</body>
</html>'''

    with open(os.path.join(DOCS_DIR, 'projects.html'), 'w') as f:
        f.write(html)
    print(f"Generated projects.html with {len(all_projects)} projects")


# === Generate individual project page ===
def generate_project_page(filepath):
    raw_name = os.path.basename(filepath).replace('.md', '')
    slug = make_slug(raw_name)

    with open(filepath, 'r') as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    html_body = render_markdown_with_mermaid(body)

    title = fm.get('title', raw_name)

    # GitHub URL for the header button
    github_url = fm.get('url', fm.get('github_url', ''))
    github_header_btn = ''
    if github_url:
        github_header_btn = f'<div style="margin-bottom:20px;"><a href="{github_url}" target="_blank" rel="noopener" class="btn-github" style="padding:10px 20px;font-size:14px;"><svg viewBox="0 0 24 24" fill="currentColor" style="width:16px;height:16px;"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.09.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg> 查看 GitHub 项目</a></div>'

    project_style = ''  # content-card styles now in external stylesheet

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>⭐</text></svg>">
{CSS}
    {project_style}
</head>
<body>
{NAV.replace('id="nav-projects"', 'id="nav-projects" class="active"')}
<main class="container">
    <a href="/projects.html" class="back-link">← 返回重点项目</a>
    <div class="content-card">
        {github_header_btn}
        {html_body}
    </div>
</main>
{FOOTER}
{MERMAID_SCRIPT}
</body>
</html>'''

    proj_html_dir = os.path.join(DOCS_DIR, 'projects')
    os.makedirs(proj_html_dir, exist_ok=True)
    with open(os.path.join(proj_html_dir, f'{slug}.html'), 'w') as f:
        f.write(html)
    print(f"Generated projects/{slug}.html")


def make_slug(name):
    """Generate project slug: remove parenthesized content, lowercase, replace non-alnum with -."""
    s = re.sub(r'\s*\([^)]*\)\s*', '', name).strip()
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


def generate_minimal_project_page(name, data, date_str):
    """Generate a minimal project detail page from daily report data."""
    slug = make_slug(name)
    proj_html_dir = os.path.join(DOCS_DIR, 'projects')
    os.makedirs(proj_html_dir, exist_ok=True)
    filepath = os.path.join(proj_html_dir, f'{slug}.html')

    url = data.get('url', '')
    desc = data.get('description', data.get('desc', ''))
    language = data.get('language', '')
    stars = data.get('stars', '')
    stars_delta = data.get('stars_delta', '')
    analysis = data.get('analysis', '')
    verdict = data.get('verdict', '')

    tags = []
    if language:
        tags.append(language)
    if verdict and '⭐' in verdict:
        tags.append('重点跟踪')
    tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags])

    meta_lines = ''
    if stars:
        meta_lines += f'<p><strong>Stars:</strong> {stars}</p>'
    if stars_delta:
        meta_lines += f'<p><strong>增速:</strong> {stars_delta}</p>'
    if url:
        meta_lines += f'<p><strong>GitHub:</strong> <a href="{url}" target="_blank">{url}</a></p>'
    if language:
        meta_lines += f'<p><strong>语言:</strong> {language}</p>'
    if verdict:
        meta_lines += f'<p><strong>判断:</strong> {verdict}</p>'
    if date_str:
        meta_lines += f'<p><strong>来源日报:</strong> <a href="/daily/{date_str}.html">{date_str}</a></p>'

    analysis_html = f'<h2>分析</h2>\n<p>{analysis}</p>' if analysis else ''

    body_html = f'''<h1>{name}</h1>
<div class="card-tags" style="margin-bottom:20px;">{tag_html}</div>
{meta_lines}
<h2>简介</h2>
<p>{desc}</p>
{analysis_html}'''

    # Add GitHub button in header for minimal pages too
    github_header_btn = ''
    if url:
        github_header_btn = f'<div style="margin-bottom:20px;"><a href="{url}" target="_blank" rel="noopener" class="btn-github" style="padding:10px 20px;font-size:14px;"><svg viewBox="0 0 24 24" fill="currentColor" style="width:16px;height:16px;"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.09.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg> 查看 GitHub 项目</a></div>'

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>⭐</text></svg>">
{CSS}
</head>
<body>
{NAV.replace('id="nav-projects"', 'id="nav-projects" class="active"')}
<main class="container">
    <a href="/trends.html" class="back-link">← 返回趋势时间线</a>
    <div class="content-card">
        {github_header_btn}
        {body_html}
    </div>
</main>
{FOOTER}
</body>
</html>'''

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"  Generated minimal project page: projects/{slug}.html")
    return slug


# === Generate trends page ===
def generate_trends():
    daily_files = sorted(glob.glob(os.path.join(DAILY_DIR, '*.md')), reverse=True)

    # Build set of existing project slugs from projects/*.md
    existing_slugs = set()
    for pf in glob.glob(os.path.join(PROJECTS_DIR, '*.md')):
        existing_slugs.add(make_slug(os.path.basename(pf).replace('.md', '')))

    # Also check docs/projects/*.html for already-generated minimal pages
    existing_html_slugs = set()
    for pf in glob.glob(os.path.join(DOCS_DIR, 'projects', '*.html')):
        existing_html_slugs.add(make_slug(os.path.basename(pf).replace('.html', '')))

    # Build slug -> url lookup from project profiles
    profile_url_map = {}
    for pf in glob.glob(os.path.join(PROJECTS_DIR, '*.md')):
        with open(pf, 'r') as f:
            c = f.read()
        fm_p, _ = parse_frontmatter(c)
        p_slug = make_slug(fm_p.get('title', fm_p.get('slug', os.path.basename(pf).replace('.md', ''))))
        p_url = fm_p.get('url', fm_p.get('github_url', None))
        if p_url:
            profile_url_map[p_slug] = p_url

    date_sections = ''
    idx = 0

    for df in daily_files:
        date_str = os.path.basename(df).replace('.md', '')
        with open(df, 'r') as f:
            content = f.read()
        fm, _ = parse_frontmatter(content)
        summary = fm.get('summary', '')
        trends = fm.get('trends', []) or []
        key_projects = fm.get('key_projects', []) or []

        is_first = (idx == 0)
        date_sections += f'''
        <div class="date-section">
            <div class="date-toggle" onclick="toggleSection('ds-{date_str}')" style="cursor:pointer;">
                <div class="date-header">
                    <span class="date-badge">{date_str}</span>
                    <span class="date-summary">{summary}</span>
                    <span class="date-arrow" id="arrow-ds-{date_str}">{'▼' if is_first else '▶'}</span>
                </div>
            </div>
            <div class="date-trends" id="ds-{date_str}" style="{'display:block;' if is_first else 'display:none;'}">
'''

        # Trend directions
        if trends:
            date_sections += '<div style="margin-bottom:16px;">'
            for t in trends:
                rank = t.get('rank', 0)
                name = t.get('name', 'Unknown')
                score_val = t.get('score', 0)
                is_high = score_val >= 55 if isinstance(score_val, int) else False
                rank_class = 'top' if rank <= 2 else ''
                score_class = 'high' if is_high else ''
                date_sections += f'''
                <div class="trend-item">
                    <div class="trend-rank {rank_class}">{rank}</div>
                    <div class="trend-content">
                        <div class="trend-title">{name}</div>
                    </div>
                    <div class="trend-score {score_class}">{score_val}/80</div>
                </div>'''
            date_sections += '</div>'

        # Key projects as cards
        if key_projects:
            date_sections += '<div class="section-title" style="margin-bottom:12px;"><span>🎯 重点项目</span></div>\n'
            date_sections += '<div class="card-grid" style="animation:none;margin-bottom:8px;">\n'
            for p in key_projects:
                pname = p.get('name', 'Unknown')
                slug = make_slug(pname)
                desc = (p.get('description', p.get('desc', '')) or '')[:80]
                language = p.get('language', '')
                stars = p.get('stars', p.get('stars_delta', ''))
                verdict = p.get('verdict', '')

                # Check if project page exists
                if slug not in existing_slugs and slug not in existing_html_slugs:
                    generate_minimal_project_page(pname, p, date_str)
                    existing_html_slugs.add(slug)

                tags = []
                if language:
                    tags.append(language)
                if verdict and '⭐' in verdict:
                    tags.append('重点跟踪')
                if not tags:
                    tags = ['项目']
                tag_html = ''.join([f'<span class="tag {tag_class(t)}">{t}</span>' for t in tags[:3]])

                # GitHub URL button - check daily data then project profiles
                github_url = p.get('url', p.get('github_url', None))
                if not github_url:
                    github_url = profile_url_map.get(slug)
                github_btn = ''
                if github_url:
                    github_btn = f'<a href="{github_url}" target="_blank" rel="noopener" class="btn-github" onclick="event.stopPropagation();"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.09.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.342-3.369-1.342-.454-1.155-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.115 2.504.337 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.202 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.163 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg>GitHub</a>'

                date_sections += f'''
                <div class="card" onclick="window.location='/projects/{slug}.html'" style="cursor:pointer">
                    <div class="card-top">
                        <div class="card-emoji">📦</div>
                        <div class="card-stars">{stars}</div>
                    </div>
                    <div class="card-title">{pname}</div>
                    <div class="card-desc">{desc}</div>
                    <div class="card-tags">{tag_html}</div>
                    <div class="card-actions">{github_btn}</div>
                </div>'''
            date_sections += '</div>\n'

        date_sections += '''
            </div>
        </div>
'''
        idx += 1

    toggle_js = '''
    <script>
    function toggleSection(id) {
        var el = document.getElementById(id);
        var arrow = document.getElementById('arrow-' + id);
        if (el.style.display === 'none') {
            el.style.display = 'block';
            arrow.textContent = '▼';
        } else {
            el.style.display = 'none';
            arrow.textContent = '▶';
        }
    }
    </script>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>趋势时间线 | GitHub 趋势研究</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><text y='20' font-size='20'>📈</text></svg>">
{CSS}
{FILTER_CSS}
</head>
<body>
{NAV.replace('id="nav-trends"', 'id="nav-trends" class="active"')}
<main class="container">
    <div class="page-header">
        <h1>📈 Trend Timeline</h1>
        <p>按日期浏览每日 GitHub 趋势研究报告</p>
    </div>
    <div class="filter-bar">
        <div class="filter-group">
            <label>🔍 搜索</label>
            <input type="text" id="trends-search" placeholder="搜索日期、项目、趋势...">
        </div>
        <span class="filter-count" id="trends-count"></span>
    </div>
{date_sections}
</main>
{FOOTER}
{toggle_js}
{TRENDS_FILTER_JS}
</body>
</html>'''

    with open(os.path.join(DOCS_DIR, 'trends.html'), 'w') as f:
        f.write(html)
    print(f"Generated trends.html with {len(daily_files)} daily entries")


# === Main ===
if __name__ == '__main__':
    print("Generating GitHub Pages HTML...")
    generate_index()
    generate_daily_list()

    for df in sorted(glob.glob(os.path.join(DAILY_DIR, '*.md'))):
        generate_daily_page(df)

    generate_projects_list()

    for pf in sorted(glob.glob(os.path.join(PROJECTS_DIR, '*.md'))):
        generate_project_page(pf)

    generate_trends()
    print("Done! All HTML pages generated.")
