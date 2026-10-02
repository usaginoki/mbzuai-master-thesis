---
title: Emergent Introspective Awareness in Large Language Models
citekey: Lindsey2025
authors: Lindsey 2025
year: 2025
published: 2025-10-29
venue: Anthropic / transformer-circuits.pub (29 Oct 2025); arXiv v1 2026-01-05
url: https://arxiv.org/abs/2601.01828
arxiv: '2601.01828'
pdf_url: https://arxiv.org/pdf/2601.01828
topics:
- misalignment-prediction
status: processing
priority: 1
relevance: core
manipulation: 'concept injection: steering vectors for known concepts added to residual-stream activations of Claude models; also prefill and instructed ''think about X'' control'
outcome: Models sometimes notice and name an injected concept, distinguish prior internal representations from text inputs, use recalled intentions to disown artificial prefills, and modulate activations on instruction; highly unreliable.
safety_use: indirect
why: 'The founding ''can it feel its own pulse'' experiment: self-report is checked against a causally manipulated internal state.'
summary: Injects known concept vectors into Claude models and asks whether the model detects an injected thought. Claude Opus 4.1 identified injected concepts roughly 20% of the time at the best layer (about two-thirds through the model) and strength, with zero false positives in 100 control trials; the author stresses that 'failures of introspection remain the norm' and that the capacity could also facilitate deception or scheming.
found_by:
- search/intro-capability
- search/intro-instrumented-feedback
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
