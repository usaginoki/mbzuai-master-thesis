---
title: 'Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents'
citekey: Zhang2026d
authors: Zhang et al. 2026
year: 2026
published: 2026-09-30
venue: arXiv preprint
url: https://arxiv.org/abs/2609.39149
arxiv: '2609.39149'
pdf_url: https://arxiv.org/pdf/2609.39149
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: '(a) offline: internal representation trajectories of the agent''s rollouts are modelled to localise turns that deviate from successful execution, then translated into textual feedback the same LLM uses to revise its skills'
outcome: Outperforms text-only skill evolution on two agent environments with two open-source LLMs where the same model is executor and optimiser (no numbers in the abstract)
safety_use: none
why: Second system that turns the model's own activations into text it then acts on, though between episodes rather than at run time
summary: Asks whether an agent can improve its external textual skills by reflecting on its own internal representations. Cites Emotion2Skill and generalises it from emotion vectors to representation trajectories. Capability only; no safety measure.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
