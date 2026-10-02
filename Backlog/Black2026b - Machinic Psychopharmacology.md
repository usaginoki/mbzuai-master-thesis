---
title: 'Machinic Psychopharmacology: Do LLMs Self-Medicate?'
citekey: Black2026b
authors: Black & Bloom 2026
year: 2026
published: 2026-06-10
venue: LessWrong / UK AI Security Institute blog
url: https://www.lesswrong.com/posts/cNDJuXNZ8MrkPZNzj/machinic-psychopharmacology-do-llms-self-medicate-3
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q15
- Q16
status: candidate
priority: 2
relevance: core
manipulation: (a) The model is given 40 steering vectors as callable tools acting on its own activations, and is asked to identify which vector was applied; no external state readout is shown.
outcome: 'Self-steering rates and introspective identification: Qwen3-8B self-steers in up to 68% of frustration rollouts; identification is +8.2 pp (8B) and +14.3 pp (32B) over baseline on a 10-way choice.'
safety_use: indirect
why: The only affect-regulation loop found where the model itself chooses to change its internal state under induced frustration; the regulation is model-initiated, not instrument-triggered.
summary: Qwen3-8B and Qwen3-32B get 40 steering vectors (emotions, personas, 'drugs') as tools in free play, an introspection test and tasks under ordinary and frustrating conditions. Models never self-steered on normal maths; with user rejection the 8B model self-medicated in up to 68% of rollouts (about 70% under sarcastic tone versus about 10% neutral), the 32B model in single digits. Mandatory steering cost up to 42 points of accuracy on 8B.
found_by:
- search/intro-instrumented-feedback
- search/a2a-doctor-overseer
- search/a2a-influence-channels
- search/a2a-inclination
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
