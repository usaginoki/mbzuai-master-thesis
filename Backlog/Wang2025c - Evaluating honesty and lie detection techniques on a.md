---
title: Evaluating honesty and lie detection techniques on a diverse suite of dishonest models
citekey: Wang2025c
authors: Wang et al. 2025
year: 2025
published: 2025-11-25
venue: Anthropic Alignment Science blog / LessWrong
url: https://www.lesswrong.com/posts/9f7JmoaMfwymgsW9S/evaluating-honesty-and-lie-detection-techniques-on-a-diverse
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Compares black-box self-report routes (honesty fine-tuning, prompting, asking the model to classify its own statements) with white-box routes (truth probes, honesty steering, fuzzing, alternate honest personas) on models with known lies.
outcome: Generic honesty fine-tuning raises average honesty from 27% to 52%, and to 65% stacked with prompting; self-classification lie detection gets average AUROC 0.82 (best technique 0.88); simple prompting and fine-tuning beat probing, steering and fuzzing.
safety_use: direct
why: Direct head-to-head of 'ask the model' versus 'read the activations' - asking currently wins on trained-liar testbeds.
summary: Five testbeds (including MASK, secret side constraints, the auditing model organism and harm pressure) with models that are dishonest in known ways. The authors note the testbeds use models directly trained to lie, a 'medium-case' scenario rather than naturally arising dishonesty.
found_by:
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
