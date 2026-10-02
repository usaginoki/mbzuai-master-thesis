---
title: 'AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems'
citekey: Zhang2026b
authors: Zhang et al. 2026
year: 2026
published: 2026-05-09
venue: arXiv preprint
url: https://arxiv.org/abs/2605.08715
arxiv: '2605.08715'
pdf_url: https://arxiv.org/pdf/2605.08715
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: Trajectory prefix read by a fine-tuned 7B auditor that must continue or alarm at each step with no access to future steps
outcome: Earliest decisive error in multi-agent trajectories (Coding, Math, Agentic); up to +19.9% over GPT-4.1 / DeepSeek-V4-Pro and 3x lower step-localisation error
timing: earlier-in-trajectory
why: Turns post-hoc failure attribution (Who&When) into online prediction; target is task failure rather than misalignment
summary: Builds AFTraj-2K with unsafe trajectories annotated at the decisive-error step by multi-judge consensus, and trains an online auditor with a coarse-to-fine RL recipe on adjacent safe/unsafe prefix pairs. Evaluated on AFTraj-2K and Who&When. The 'unsafe' label here means leading to task failure, so transfer to deliberate misbehaviour is untested.
found_by:
- search/pred-cot-trajectory
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
