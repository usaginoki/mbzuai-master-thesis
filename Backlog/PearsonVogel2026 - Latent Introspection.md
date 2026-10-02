---
title: 'Latent Introspection: Models Can Detect Prior Concept Injections'
citekey: PearsonVogel2026
authors: Pearson-Vogel et al. 2026
year: 2026
published: 2026-02-23
venue: arXiv preprint
url: https://arxiv.org/abs/2602.20031
arxiv: '2602.20031'
pdf_url: https://arxiv.org/pdf/2602.20031
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: concept injection into earlier context of Qwen2.5-Coder-32B; logit lens on the residual stream; prompt giving accurate information about introspection
outcome: The model verbally denies injection but the residual stream carries a detection signal that is attenuated in final layers; informing the model about introspection unmasks it.
safety_use: indirect
why: 'The internal signal exists before it is reported: self-report under-reads the ''pulse'', and prompting changes that.'
summary: Sensitivity to injection rises from 0.3% to 39.9% with only a 0.6% increase in false positives when the prompt explains AI introspection mechanisms; mutual information between nine injected and recovered concepts rises from 0.61 to 1.05 bits, arguing against a generic-noise explanation.
found_by:
- search/intro-capability
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
