---
title: 'LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception'
citekey: Xu2026b
authors: Xu et al. 2026
year: 2026
published: 2026-06-29
venue: arXiv preprint
url: https://arxiv.org/abs/2606.30005
arxiv: '2606.30005'
pdf_url: https://arxiv.org/pdf/2606.30005
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: No activations. A runtime dashboard of the agent's own context state (per-block token usage, recency, access history, remaining budget) is surfaced in the prompt (VISTA).
outcome: Training-free dashboard improves long-horizon tool agents; lifts Gemini-3-Flash on LOCA-Bench from 22.7% to 50.7% (abstract).
safety_use: none
why: Same 'show the agent its own state' pattern under the name state proprioception; capability only.
summary: Argues agents are 'proprioceptively blind' to their own context and shows a visible state dashboard improves four backbones, e.g. 22.7% to 50.7% for Gemini-3-Flash on LOCA-Bench. Abstract-level read plus a check of the headline number; ablations not read.
found_by:
- search/intro-i1-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
