#!/usr/bin/env python3
"""
github-researcher 完整性验证脚本
输出 JSON 格式的检查结果，供子代理判断

用法: python3 skills/github-daily/scripts/validate.py
退出码: 0=通过, 1=有错误
"""

import json, glob, os, re, sys, yaml

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
DAILY = os.path.join(BASE, 'daily')
PROJECTS = os.path.join(BASE, 'projects')
DOCS = os.path.join(BASE, 'docs')
INDEXES = os.path.join(BASE, 'indexes')
DAILY_REPORT = os.path.join(BASE, 'daily-report.md')

results = {"pass": True, "errors": [], "warnings": [], "stats": {}, "gaps": []}

# === 1. Daily MD 完整性 ===
daily_files = sorted(glob.glob(os.path.join(DAILY, '*.md')))
results["stats"]["dailies"] = len(daily_files)

for df in daily_files:
    basename = os.path.basename(df)
    with open(df) as f:
        content = f.read()
    
    if not content.startswith('---'):
        results["errors"].append(f"{basename}: 缺少 YAML frontmatter")
        results["pass"] = False
        continue
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        results["errors"].append(f"{basename}: frontmatter 格式错误")
        results["pass"] = False
        continue
    
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        results["errors"].append(f"{basename}: frontmatter YAML 解析失败")
        results["pass"] = False
        continue
    
    # 必填字段检查
    required = ['title', 'date', 'summary']
    for field in required:
        if not fm.get(field):
            results["errors"].append(f"{basename}: frontmatter 缺少必填字段 '{field}'")
            results["pass"] = False
    
    # summary 是核心主题，不能太短
    summary = fm.get('summary', '')
    if summary and len(summary) < 10:
        results["warnings"].append(f"{basename}: summary 过短 ({len(summary)} chars)")
    
    # 检查 trends 和 key_projects
    trends = fm.get('trends', [])
    if not trends:
        results["warnings"].append(f"{basename}: 没有 trends 数据")
    
    key_projects = fm.get('key_projects', [])
    if not key_projects:
        results["warnings"].append(f"{basename}: 没有 key_projects")
    else:
        # 记录项目名，后续与 projects/ 对比
        for kp in key_projects:
            pname = kp.get('name', '')
            if pname:
                # 去掉括号内的 org 信息，如 "claw-code (ultraworkers)" → "claw-code"
                clean_name = re.sub(r'\s*\([^)]*\)', '', pname).strip()
                slug = re.sub(r'[^a-z0-9]+', '-', clean_name.lower()).strip('-')
                profile_path = os.path.join(PROJECTS, f'{slug}.md')
                if not os.path.exists(profile_path):
                    # 尝试模糊匹配：去掉所有分隔符后比较
                    found = False
                    clean_key = clean_name.lower().replace('-', '').replace(' ', '').replace('_', '').replace('.', '')
                    for pf in os.listdir(PROJECTS) if os.path.isdir(PROJECTS) else []:
                        pf_key = pf.replace('.md', '').lower().replace('-', '').replace(' ', '').replace('_', '')
                        if clean_key in pf_key or pf_key in clean_key:
                            found = True
                            break
                    if not found:
                        results["gaps"].append({"type": "missing_project_profile", "project": pname, "source": basename})
                        results["errors"].append(f"{basename}: key_project '{pname}' 没有 projects/*.md 档案")
                        results["pass"] = False

    # 文件大小
    if os.path.getsize(df) < 2000:
        results["warnings"].append(f"{basename}: 文件偏小 ({os.path.getsize(df)} bytes)")

# === 2. Projects 档案完整性 ===
project_files = sorted(glob.glob(os.path.join(PROJECTS, '*.md')))
results["stats"]["projects"] = len(project_files)

for pf in project_files:
    basename = os.path.basename(pf)
    size = os.path.getsize(pf)
    if size < 500:
        results["warnings"].append(f"{basename}: 文件过小 ({size} bytes)，可能是空壳")
    
    with open(pf) as f:
        content = f.read()
    if not content.startswith('---'):
        results["errors"].append(f"{basename}: 缺少 frontmatter")
        results["pass"] = False
        continue
    
    parts = content.split('---', 2)
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except:
        continue
    
    # 检查关键字段
    for field in ['title', 'category']:
        if not fm.get(field):
            results["warnings"].append(f"{basename}: 缺少 '{field}' 字段")

# === 3. HTML 同步 ===

# 每个 daily MD 应该有对应的 HTML
for df in daily_files:
    name = os.path.basename(df).replace('.md', '')
    html_path = os.path.join(DOCS, 'daily', f'{name}.html')
    if not os.path.exists(html_path):
        results["errors"].append(f"缺少 docs/daily/{name}.html")
        results["gaps"].append({"type": "missing_daily_html", "date": name})
        results["pass"] = False

# 每个 project MD 应该有对应的 HTML
for pf in project_files:
    name = os.path.basename(pf).replace('.md', '')
    html_path = os.path.join(DOCS, 'projects', f'{name}.html')
    if not os.path.exists(html_path):
        results["errors"].append(f"缺少 docs/projects/{name}.html")
        results["gaps"].append({"type": "missing_project_html", "project": name})
        results["pass"] = False

# 核心页面存在性
for page in ['index.html', 'daily.html', 'trends.html', 'projects.html']:
    path = os.path.join(DOCS, page)
    if not os.path.exists(path):
        results["errors"].append(f"缺少 docs/{page}")
        results["pass"] = False
    elif os.path.getsize(path) < 500:
        results["errors"].append(f"docs/{page} 文件异常（过小）")
        results["pass"] = False

# generate_pages.py 存在
if not os.path.exists(os.path.join(DOCS, 'generate_pages.py')):
    results["errors"].append("缺少 docs/generate_pages.py")
    results["pass"] = False

# === 4. trend-index.md ===
trend_index = os.path.join(INDEXES, 'trend-index.md')
if os.path.exists(trend_index):
    with open(trend_index) as f:
        ti_content = f.read()
    # 检查最近 3 天是否有条目
    import datetime
    for i in range(3):
        date = (datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        if date not in ti_content:
            results["warnings"].append(f"trend-index.md 缺少 {date} 的条目")
else:
    results["errors"].append("缺少 indexes/trend-index.md")
    results["pass"] = False

# === 5. daily-report.md ===
if os.path.exists(DAILY_REPORT):
    with open(DAILY_REPORT) as f:
        dr_content = f.read()
    # 检查最近 3 天是否有核心主题
    import datetime
    for i in range(3):
        date = (datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        if date not in dr_content:
            results["warnings"].append(f"daily-report.md 缺少 {date} 的条目")
else:
    results["warnings"].append("缺少 daily-report.md")

# === 6. HTML 嵌套 <a> 标签检查 ===
nested_a_pattern = re.compile(r'<a[^>]*class="card"')
for html_file in glob.glob(os.path.join(DOCS, '*.html')):
    with open(html_file) as f:
        content = f.read()
    if nested_a_pattern.search(content):
        page = os.path.basename(html_file)
        results["errors"].append(f"{page}: 发现嵌套 <a> 标签（card wrapper 是 <a>），会导致 GitHub 链接变形")
        results["pass"] = False

# === 7. 首页 stats 动态计算验证 ===
index_html = os.path.join(DOCS, 'index.html')
if os.path.exists(index_html):
    with open(index_html) as f:
        idx = f.read()
    # 检查 generate_pages.py 是否使用动态 stats
    gen_py = os.path.join(DOCS, 'generate_pages.py')
    if os.path.exists(gen_py):
        with open(gen_py) as f:
            gen_content = f.read()
        if 'aggregate_all_projects' in gen_content and 'Dynamic stats' in gen_content:
            pass  # 好的，使用动态计算
        else:
            results["warnings"].append("generate_pages.py 可能未使用动态 stats 计算")

# === 输出 ===
print(json.dumps(results, ensure_ascii=False, indent=2))
sys.exit(0 if results["pass"] else 1)
