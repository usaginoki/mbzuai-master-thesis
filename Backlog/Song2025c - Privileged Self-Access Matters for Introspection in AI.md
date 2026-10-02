---
title: Privileged Self-Access Matters for Introspection in AI
citekey: Song2025c
authors: Song et al. 2025
year: 2025
published: 2025-08-20
venue: arXiv preprint
url: https://arxiv.org/abs/2508.14802
arxiv: '2508.14802'
pdf_url: https://arxiv.org/pdf/2508.14802
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Self-report of sampling temperature after generating a sentence; validated against the true setting and against within-model and across-model third-party prediction from the prompt and output
outcome: Models answer HIGH for 'crazy' sentences and LOW for 'factual' ones regardless of the actual temperature; self-reflection accuracy is not higher than across-model prediction.
safety_use: indirect
why: 'Gives the definition I2''s privileged-increment test operationalises: beat a third party of equal or lower computational cost'
summary: Song, Lederman, Hu, Mahowald define introspection as a process yielding information about internal states 'more reliable than one with equal or lower computational cost available to a third party'. Tested on GPT-4o, GPT-4.1, Gemini-2.0-flash and Gemini-2.5-flash with temperatures 0 to 2.0.
found_by:
- search/intro-i2-search
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
