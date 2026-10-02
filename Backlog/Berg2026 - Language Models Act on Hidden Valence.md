---
title: Language Models Act on Hidden Valence
citekey: Berg2026
authors: Berg and Kaiser 2026
year: 2026
published: 2026-09-28
venue: arXiv preprint
url: https://arxiv.org/abs/2609.35591
arxiv: '2609.35591'
pdf_url: https://arxiv.org/pdf/2609.35591
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: 'No instrument shown to the model. Experimenter steers a valence direction; in the last experiment the model gets tools adjust_context(intensity), reset_context() and log_status(note) and is NOT told what the adjustment does; it can only notice its own state from its outputs: (d) unaided, plus self-steering tools'
outcome: Revealed preference for valenced hidden states across seven open-weight models; with self-steering tools (OLMo-2-32B only) the model removes imposed negative steering about 35% of the time at dose -1 and about 21% at -0.5, versus about 7% for random directions and 4-5% for positive steering
safety_use: indirect
why: Model given a tool to regulate its own internal state and uses it selectively to leave a negative one; complements Black2026 (self-medication)
summary: Valence steering attached to an arbitrary 'zone' shifts later choice even when all visible tokens are identical and only the KV cache differs; the effect is nearly absent in a base model and emerges during DPO. Given tools to steer itself, the model rarely self-administers positive steering (13.5% vs 10% no-steering baseline, p=0.35) but reliably removes an imposed negative state in a dose-dependent way. The self-steering experiment uses one model and does not separate text from hidden-state channels.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
