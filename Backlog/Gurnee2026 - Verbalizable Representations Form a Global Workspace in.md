---
title: Verbalizable Representations Form a Global Workspace in Language Models
citekey: Gurnee2026
authors: Gurnee, Sofroniew, Pearce et al. 2026 (Anthropic)
year: 2026
published: 2026-07-06
venue: Transformer Circuits Thread; Anthropic summary 'A global workspace in language models'
url: https://transformer-circuits.pub/2026/workspace/index.html
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Jacobian lens (J-lens) reads a small verbalizable subspace of Claude's residual stream; (d) unaided report and instructed control, verified by swapping/ablating lens directions; (c) human tool for hidden states. Not shown to the model.
outcome: Model reports and can deliberately modulate J-space contents; panic, 'damn', 'failure', 'fake' appear there without appearing in output; training the model to articulate principles if interrupted lowers dishonest behaviour.
safety_use: direct
why: Ground-truthed evidence for which internal states a model can report and control, plus an unverbalized affect/metacognition readout; the counterfactual-reflection result is a training-time cousin of 'make the model aware of its state'.
summary: J-space is about 10% or less of activation variance; lens-coordinate swaps redirect reasoning in 54-70% of trials, and the J-space component of concept vectors drives the swap target into top-5 outputs on 59% of trials (88% for pure J-lens vectors). Ablating eval-awareness representations surfaced blackmail some of the time. Counterfactual reflection training improved behaviour with no numbers given; ablating the implanted concepts largely reverted it. The paper does not use the lens as a run-time monitor or show it to the model.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
