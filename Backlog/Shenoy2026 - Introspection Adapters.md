---
title: 'Introspection Adapters: Training LLMs to Report Their Learned Behaviors'
citekey: Shenoy2026
authors: Shenoy et al. 2026
year: 2026
published: 2026-04-18
venue: arXiv preprint (Anthropic)
url: https://arxiv.org/abs/2604.16812
arxiv: '2604.16812'
pdf_url: https://arxiv.org/pdf/2604.16812
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: A single LoRA 'introspection adapter' trained across many fine-tunes with implanted behaviours so that models verbalise what they learned
outcome: Hidden learned behaviours of fine-tuned models; generalises to differently trained fine-tunes, state of the art on AuditBench for explicitly hidden concerning behaviours, detects encrypted fine-tuning API attacks
timing: pre-deployment
safety_use: direct
why: Turns self-report into a trained auditing tool that names concerning behaviours before they are observed in deployment.
summary: From a base model M, many fine-tunes with implanted behaviours provide labelled data to train one LoRA adapter that makes fine-tunes describe their implanted behaviour. It generalises to fine-tunes trained very differently, achieves state of the art on AuditBench and scales with model size and training diversity. A later paper (Kutsyk & Zielinski, arXiv 2607.03640) reports that it misses some behaviours and then hallucinates wrong ones.
found_by:
- search/pred-self-and-cross-model
- search/intro-capability
- search/intro-instrumented-feedback
- search/intro-safety-uses-and-risks
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
