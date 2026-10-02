---
title: Mechanisms of Introspective Awareness
citekey: Macar2026
authors: Macar et al. 2026
year: 2026
published: 2026-03-22
venue: arXiv preprint
url: https://arxiv.org/abs/2603.21396
arxiv: '2603.21396'
pdf_url: https://arxiv.org/pdf/2603.21396
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: steering-vector injection in open-weight models (mainly Gemma3-27B; also Qwen3-235B, OLMo-3.1-32B); circuit tracing, refusal-direction ablation, trained bias vector
outcome: Detection is behaviourally robust with 0% false positives, emerges from post-training (DPO-like preference optimisation, not plain SFT), runs through 'evidence carrier' features suppressing default-'no' 'gate' features, and is strongly under-elicited.
safety_use: indirect
why: Best mechanistic account of how a model senses an internal perturbation, and shows the 'sensor' can be amplified.
summary: On Gemma3-27B (layer 37, strength 4) baseline detection is 10.8% with 0% false positives; ablating the refusal direction raises detection to 63.8% with false positives rising to 7.3%, and a trained bias vector adds about 75% detection on held-out concepts with no false positives. Identification of the concept uses largely distinct later-layer mechanisms; the circuit is absent in base models. Authors flag dual-use risk and recommend treating self-reported detection as auxiliary, not authoritative.
found_by:
- search/intro-capability
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
