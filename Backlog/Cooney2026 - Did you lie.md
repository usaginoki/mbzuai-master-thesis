---
title: '"Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms'
citekey: Cooney2026
authors: Cooney, Africa et al. 2026 (UK AISI)
year: 2026
published: 2026-06-10
venue: arXiv preprint / UK AISI research page
url: https://www.aisi.gov.uk/research/did-you-lie-evaluating-lie-detectors-across-model-scale-and-belief-verified-model-organisms
arxiv: '2606.12618'
pdf_url: https://arxiv.org/pdf/2606.12618
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: CoT judge and activation probes including a 'Did-You-Lie' follow-up-question probe; (c) evaluator tool, not returned to the model.
outcome: Detectors scale with capability on prompted lies across 31 models but degrade on trained organisms with verified hidden beliefs; best is CoT judge at 0.82 balanced accuracy.
safety_use: direct
why: Calibrates how much any deception readout could be trusted before feeding it back to an agent.
summary: 31 open-weight models from 2B to 1T parameters and 13 reasoning model organisms with belief-verified hidden beliefs. All four detector types improved with scale on prompted lying but dropped on trained organisms. Authors conclude current lie detectors cannot support high-confidence claims about model beliefs.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
