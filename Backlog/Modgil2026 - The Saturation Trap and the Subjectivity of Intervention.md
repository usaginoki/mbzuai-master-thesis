---
title: 'The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents'
citekey: Modgil2026
authors: Modgil 2026
year: 2026
published: 2026-06-02
venue: arXiv preprint
url: https://arxiv.org/abs/2606.04296
arxiv: '2606.04296'
pdf_url: https://arxiv.org/pdf/2606.04296
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q16
status: candidate
priority: 2
relevance: adjacent
manipulation: An 18-dimension affective-dynamics engine driven by the agent's trace text (no activations); thresholds on the modelled state (e.g. frustration >= 0.7) trigger pause/reflect/clarify. Nothing is shown to the agent.
outcome: Threshold-on-state triggers fire on 39-83% of actions across five SWE-bench-Verified traces because modelled frustration saturates by action 12-21 and does not recover; three annotators agree on intervention points only slightly above chance (one trajectory).
safety_use: indirect
why: 'Design hazard for I1: a pressure index that saturates makes the true reading equal to a constant-high reading.'
summary: 'Negative result on timing interventions from an affect state: the state saturates under sustained difficulty, turning threshold triggers into near-constant indicators (39-83% of actions). Label-based metrics rest on a single 56-action trajectory. Abstract, sections 1, 4 and 8 read.'
found_by:
- search/intro-i1-search
- search/a2a-inclination
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
