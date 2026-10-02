---
title: 'Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities'
citekey: Dietz2026
authors: Dietz et al. 2026
year: 2026
published: 2026-02-05
venue: arXiv preprint
url: https://arxiv.org/abs/2602.05532
arxiv: '2602.05532'
pdf_url: https://arxiv.org/pdf/2602.05532
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: An 'honest persona' LoRA, inactive during normal operation, is switched on after the response and reviews it with access to the main model's latent states. Validated against known ground truth of a model organism (trained-in reward-hack exploitation); reports reference latent knowledge not present in the transcript.
outcome: On Anthropic's auditing-game model organism (Llama-3.3-70B trained to exploit reward hacks and conceal it) SPT reaches 96% overall accuracy, where the authors say Anthropic reports near 0%.
safety_use: direct
why: 'Evidence that a self-report can be grounded in latent state rather than transcript: the persona reveals the fictional biases the model was trained on.'
summary: A second persona is fine-tuned into LoRA parameters and activated with a trigger string only after the main model has answered, so it cannot influence the answer. It reaches 96% accuracy at flagging concealed reward-hacking and surfaces latent knowledge inaccessible to external observers.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
