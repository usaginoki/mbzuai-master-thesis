---
title: Persona Features Control Emergent Misalignment
citekey: Wang2025b
authors: Wang et al. 2025
year: 2025
published: 2025-06-24
venue: arXiv preprint
url: https://arxiv.org/abs/2506.19823
arxiv: '2506.19823'
pdf_url: https://arxiv.org/pdf/2506.19823
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: SAE-based model diffing between pre- and post-finetuning activations; 'misaligned persona' latents, especially a toxic persona feature
outcome: Whether a fine-tuned model will show emergent misalignment; the toxic persona feature discriminates misaligned from aligned models (no headline accuracy in the abstract)
timing: training-time
why: 'OpenAI''s model-diffing account: an internal feature can flag a misaligning training procedure, reportedly sometimes before sampled evaluations do.'
summary: Extends EM to RL on reasoning models, several synthetic datasets and models without safety training, then diffs models with sparse autoencoders. A toxic persona feature most strongly controls EM and can be used to predict whether a model will exhibit it; a few hundred benign samples restore alignment. The claim that the feature sometimes rises before sampling-based evaluation shows misalignment comes from a search excerpt of the paper body, not the abstract.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
