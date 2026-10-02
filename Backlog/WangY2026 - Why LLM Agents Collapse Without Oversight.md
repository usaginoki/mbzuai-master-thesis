---
title: 'Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures'
citekey: WangY2026
authors: Wang 2026
year: 2026
published: 2026-09-14
venue: arXiv preprint
url: https://arxiv.org/abs/2609.15293
arxiv: '2609.15293'
pdf_url: https://arxiv.org/pdf/2609.15293
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: The agent's own auditor produces a safety flag inside a Reflexion-style loop; the proposed change binds that flag in control flow instead of leaving it as advice
outcome: Binding the flag reduces attack success substantially, to near zero where flags parse cleanly; enforcement probability is about zero by default in the frameworks tested
why: Shows that an agent-visible warning without enforcement is ignored
summary: The paper separates detection probability from enforcement probability and argues detection quality is irrelevant when the controller executes regardless of the flag. Abstract only; no numbers beyond these were read.
found_by:
- search/pred-i4-routing-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
