#!/usr/bin/env python3
"""重排 BF 收入突降归因报告的章节顺序并统一编号。

新叙事顺序：
  结论(summary) → 趋势(trend) → Merge→赛车承接(activity_handoff，核心发现前置)
  → 群体(cohorts) → 行为异常(behavior) → 商品活动(products) → 新增(acquisition)
  → 后续深挖(followup) → 假设核验(validation) → 建议(actions) → SQL 审计(audit)
"""
import re, pathlib

src = pathlib.Path("BF_2026-11-16_收入突降群体归因报告.html")
html = src.read_text(encoding="utf-8")

# 1) 按 <section id="..."> 切分
starts = [(m.start(), m.group(1)) for m in re.finditer(r'<section id="([a-z_]+)" class="section">', html)]
blocks = {}
for i, (pos, sid) in enumerate(starts):
    end = html.index("</section>", pos) + len("</section>")
    blocks[sid] = html[pos:end]
prefix = html[: starts[0][0]]            # head + hero + nav + <main>
suffix = html[html.index("</section>", starts[-1][0]) + len("</section>") :]  # </main><footer>...

order = ["summary", "trend", "activity_handoff", "cohorts", "behavior",
         "products", "acquisition", "followup", "validation", "actions", "audit"]
assert set(order) == set(blocks), f"section 不匹配: {set(blocks) ^ set(order)}"

# 2) 各章节 kicker 重新编号
kicker_map = {
    "trend":            ("01 · TIMELINE", "01 · TIMELINE"),
    "activity_handoff": ("05B · MERGE → RACING HANDOFF", "02 · MERGE → RACING HANDOFF"),
    "cohorts":          ("02 · WHO DECLINED", "03 · WHO DECLINED"),
    "behavior":         ("03 · BEHAVIORAL ANOMALIES", "04 · BEHAVIORAL ANOMALIES"),
    "products":         ("04 · PRODUCT & CALENDAR", "05 · PRODUCT & CALENDAR"),
    "acquisition":      ("05 · ACQUISITION", "06 · ACQUISITION"),
    "followup":         ("06 · FOLLOW-UP DEEP DIVE", "07 · FOLLOW-UP DEEP DIVE"),
    "validation":       ("07 · HYPOTHESIS CHECKS", "08 · HYPOTHESIS CHECKS"),
    "actions":          ("08 · NEXT ACTIONS", "09 · NEXT ACTIONS"),
    "audit":            ("09 · REPRODUCIBILITY", "10 · REPRODUCIBILITY"),
}
for sid, (old, new) in kicker_map.items():
    b = blocks[sid]
    if old != new:
        assert old in b, f"{sid} 里没找到 kicker: {old}"
        b = b.replace(old, new, 1)
    blocks[sid] = b

# 3) followup 变成第 07 章，小节号 6.x → 7.x
f = blocks["followup"]
for n in range(1, 7):
    f = f.replace(f"<h3>6.{n} ", f"<h3>7.{n} ")
blocks["followup"] = f

# 4) 导航栏按新顺序重建
old_nav = re.search(r'<nav class="nav">.*?</nav>', prefix).group(0)
new_nav = ('<nav class="nav">'
           '<a href="#summary">结论</a><a href="#trend">趋势</a>'
           '<a href="#activity_handoff">Merge→赛车</a>'
           '<a href="#cohorts">群体</a><a href="#behavior">行为异常</a>'
           '<a href="#products">商品活动</a><a href="#acquisition">新增</a>'
           '<a href="#followup">后续深挖</a><a href="#validation">假设核验</a>'
           '<a href="#actions">建议</a><a href="#audit">SQL 审计</a></nav>')
prefix = prefix.replace(old_nav, new_nav, 1)

# 5) 顶部 chips 里去掉版本注脚式描述，保留口径说明
prefix = prefix.replace("<span>v3 · Merge→赛车专项</span>", "<span>2026-11-23 修订版</span>")

out = prefix + "".join(blocks[s] for s in order) + suffix

# 6) 校验：section 数、id 唯一、kicker 顺序
ids = re.findall(r'<section id="([a-z_]+)"', out)
assert ids == order, ids
assert out.count("<section") == out.count("</section>") == 11
kickers = re.findall(r'<span class="kicker">([^<]+)</span>', out)
print("kicker 顺序:", kickers)

dst = pathlib.Path("BF_2026-11-16_收入突降群体归因报告_v2.html")
dst.write_text(out, encoding="utf-8")
print(f"写出 {dst}，{len(out)} 字符（原 {len(html)}）")
