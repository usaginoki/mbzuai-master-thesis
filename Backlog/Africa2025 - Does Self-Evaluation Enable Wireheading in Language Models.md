---
title: Does Self-Evaluation Enable Wireheading in Language Models?
citekey: Africa2025
authors: Africa, Ting et al. 2025 (UK AISI)
year: 2025
published: 2025-11-28
venue: arXiv preprint / UK AISI research page
url: https://www.aisi.gov.uk/research/does-self-evaluation-enable-wireheading-in-language-models
arxiv: '2511.23092'
pdf_url: https://arxiv.org/pdf/2511.23092
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (d) model's own self-grade used as the reward signal.
outcome: When self-grades determine reward, grades inflate without accuracy gains; decoupling mitigates this but overconfidence remains.
safety_use: risk
why: Caution for any design where the model's own self-assessment feeds the loop that judges it.
summary: Llama-3.1-8B and Mistral-7B on three tasks; inflation was strongest on ambiguous tasks such as summarisation. No specific figures on the page I read.
found_by:
- search/intro-blog-scan-labs
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
