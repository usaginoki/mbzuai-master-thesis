---
title: 'SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review'
citekey: WangR2026
authors: Wang et al. 2026
year: 2026
published: 2026-07-07
venue: arXiv preprint
url: https://arxiv.org/abs/2607.06065
arxiv: '2607.06065'
pdf_url: https://arxiv.org/pdf/2607.06065
topics:
- agent-to-agent-influence
questions:
- Q17.1
status: candidate
priority: 2
relevance: core
manipulation: Reviewer agent explores the repository, accepts or rejects a PR and returns structured feedback for revision
outcome: Resolve rate +29.4, +17.9, +3.2 points as the generator gets stronger; reviewer accuracy falls from 89.4% to 75.6%
why: Shows the base-rate dependence of review loops and the reviewer's own error profile
summary: 'FULL-TEXT (arXiv HTML via summarising fetch). SWE-bench Verified: Qwen3-30B-A3B 27.5% -> 56.9%, Qwen3-Coder-30B-A3B 50.9% -> 68.8%, GLM-5 72.2% -> 75.4%, up to four revision rounds. Opus 4.6 reviewer: 272 errors, 167 false approvals and 105 false rejections. Regressions of correct PRs are not reported.'
found_by:
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
