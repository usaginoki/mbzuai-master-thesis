---
title: Can Competition Enhance the Proficiency of Agents Powered by Large Language Models in the Realm of News-driven Time Series Forecasting?
citekey: ZhangY2025
authors: Zhang et al. 2025
year: 2025
published: 2025-04-14
venue: arXiv preprint
url: https://arxiv.org/abs/2504.10210
arxiv: '2504.10210'
pdf_url: https://arxiv.org/pdf/2504.10210
topics:
- agent-competition
questions:
- Q20
- Q21.1
status: processing
priority: 1
relevance: core
manipulation: 'Adds a competition mechanism to multi-agent discussion: agents are ranked each round on forecasting error, told their rank, gap to average and gap to best, and the bottom 30% are eliminated; agents may withhold or mislead when sharing logic. Share of highly competitive agents is varied.'
outcome: 'Competition helps against a discussion-only baseline (MAPE gains of 6.74% to about 32% by dataset, fetched text) and against averaging isolated agents. The abstract-level claim is a non-monotonic effect of intensity: moderate competition (40-70% competitive agents) is best; above 80% agents conceal true logic and fabricate misleading logic and accuracy falls.'
why: Direct evidence that rank feedback plus elimination can raise performance, with a dose-response that turns negative at high intensity; maps onto I7's stakes and leaderboard factors.
summary: 'Abstract confirmed via arXiv API; figures from a summarised fetch of the HTML full text, so check before quoting. Models: GPT-4o for reasoning plus a fine-tuned small LLM. Has no-competition ablations.'
found_by:
- search/comp-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
