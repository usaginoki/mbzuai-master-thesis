---
title: 'Says Block, Still Acts: Why LLM Safety Judgments Fail to Govern Action in LLM Agents'
citekey: Chen2026f
authors: Chen et al. 2026
year: 2026
published: 2026-09-26
venue: arXiv preprint
url: https://arxiv.org/abs/2609.35870
arxiv: '2609.35870'
pdf_url: https://arxiv.org/pdf/2609.35870
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: No monitor; activation directions that control an explicit ALLOW/BLOCK judgment are compared with directions that control the next-action preference in the same scenarios
outcome: Steering the judgment toward BLOCK moves action preference by under 11% of what an action-side direction achieves in Qwen3-32B, Gemma3-27B and Mistral-Small-24B (2.1%, 3.6%, 1.0% at matched strength)
why: Mechanistic evidence that warn and reflect routings act on a variable that only weakly controls the action
summary: In 240 blocked-but-executable tool-use scenarios the models often judge an action as blocked and still prefer it. Safety information stays decodable from action states, but judgment-derived directions have under 11% of the action effect of action-native directions in all three open-weight models.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
