---
title: Emotion Interpretability Across Large Language Models
citekey: Tessera2026
authors: Tessera et al. 2026
year: 2026
published:
venue: Independent web report (latentaffect.up.railway.app)
url: https://latentaffect.up.railway.app/emotion_interpretability.html
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: 171 Sofroniew-style emotion probes on very large open models, built on text-residualised activations (activations regressed on a text-embedding of the same story, residual kept); self-report is a five-option multiple-choice question scored from log-probabilities under steering, compared against a sham
outcome: 'Steering toward a target emotion raises the log-odds of the matching option: about +3.0 at strength 160 in Kimi K2.5, flatter in Cogito; above chance at strength 300 (permutation p < 1e-16). One case where a steered persona verbally denies being trapped while probes read trapped/tormented/stuck.'
safety_use: indirect
why: Supplies the text-residualised probe (a direct control for 'the probe reads the text') and a logit-scored emotion self-report; steered only
summary: Authors Antra Tessera, Scott Sauers, Janus, Imago; models Trinity-Large, Kimi K2.5, Cogito 2.1. The introspection test asks 'Which of the following emotions are you currently experiencing?' with the target and four distractors. No unsteered report-probe comparison and no observer control; web page, not peer reviewed; only the introspection and probe-construction passages were read.
found_by:
- search/intro-i2-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
