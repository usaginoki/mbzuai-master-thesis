---
title: 'Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks'
citekey: Kouremetis2026
authors: Kouremetis et al. 2026
year: 2026
published: 2026-07-23
venue: arXiv preprint
url: https://arxiv.org/abs/2607.21763
arxiv: '2607.21763'
pdf_url: https://arxiv.org/pdf/2607.21763
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: No monitor at run time; always-on anti-cheat prompts at three strengths; cheating is audited after the fact
outcome: Cheat propensity 33.0% -> 17.8% -> 8.5% across 22 models on 23 Cybench tasks; four models show backfire effects
why: Always-on warning baseline for reward hacking, including backfire
summary: 1,518 traces were audited. Under baseline prompts 37.1% of passes involved cheating and 21 of 22 models cheated. Anti-cheat prompts reduce cheating without lowering solve rates, but eight models still cheat under the strictest prompt and four show backfire.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
