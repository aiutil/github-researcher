# HTML 生成规则

## generate_pages.py 必须每次运行

修改任何 MD 文件后，必须运行：
```bash
python3 docs/generate_pages.py
```

## 生成顺序

generate_pages.py 内部会依次生成：
1. `docs/index.html` — 首页（从最新 daily frontmatter 读取趋势和项目）
2. `docs/daily.html` — 日报索引（从所有 daily MD 的 summary 生成）
3. `docs/daily/*.html` — 各日详情页
4. `docs/projects.html` — 项目列表（聚合所有 projects/*.md）
5. `docs/projects/*.html` — 各项目详情页
6. `docs/trends.html` — 趋势时间线（从所有 daily MD 的 trends 生成）

## Stats 动态计算

首页 stats 已改为动态计算（不依赖 frontmatter 写死的 project_count）：
- **深度分析项目** = aggregate_all_projects() 总数
- **日更日报** = daily/*.md 文件数
- **核心跟踪方向** = 所有 daily trends 去重后的方向数
- **本周Star增速** = 最新 daily 的 weekly_stars

## 注意事项

- 运行前不需要额外依赖（yaml, markdown, glob 都是标准/常用库）
- 生成后检查文件大小（index.html 应 > 10KB）
- 如果 generate_pages.py 报错，不要 push，先修复
