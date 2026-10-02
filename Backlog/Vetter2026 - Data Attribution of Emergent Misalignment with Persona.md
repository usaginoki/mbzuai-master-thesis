---
title: Data Attribution of Emergent Misalignment with Persona Features
citekey: Vetter2026
authors: Vetter et al. 2026
year: 2026
published: 2026-08-11
venue: arXiv preprint
url: https://arxiv.org/abs/2608.11025
arxiv: '2608.11025'
pdf_url: https://arxiv.org/pdf/2608.11025
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: SAE model diffing to find persona features; attribution of those features to one million pre-training web documents
outcome: 'Negative for data-content prediction: the retrieved human-written documents do not reliably induce EM, while synthetic instruction-response pairs from the same content do'
timing: training-time
why: Shows semantic relevance of data to a 'bad persona' feature is not sufficient to predict that the data will misalign a model.
summary: Across four open-weight models, misalignment fine-tuning amplifies jailbreak-persona, sarcasm, deception and manipulation features; steering single features induces misalignment rates up to 62% (vs. 35% from fine-tuning) and can realign models. Fine-tuning on the attributed human-written documents does not reliably induce EM, whereas derived synthetic pairs do and transfer across families.
found_by:
- search/pred-training-time
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
