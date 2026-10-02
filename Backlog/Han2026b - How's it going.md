---
title: How's it going? Reinforcement learning in language models recruits a functional welfare axis
citekey: Han2026b
authors: Han et al. 2026
year: 2026
published: 2026-05-28
venue: arXiv preprint; LessWrong summary 2026-05-30
url: https://arxiv.org/abs/2605.30232
arxiv: '2605.30232'
pdf_url: https://arxiv.org/pdf/2605.30232
topics:
- misalignment-prediction
status: candidate
priority: 3
relevance: adjacent
manipulation: (c) concept vectors for rewarded and punished trajectories extracted after RL in a semantically neutral emoji maze; used for steering and analysis, not shown to the model
outcome: The punishment vector aligns with negative emotion concepts and, when steered, induces negative self-reports, pathological backtracking, refusal and uncertainty; the axis pre-exists post-training
safety_use: indirect
why: Candidate 'how well am I doing' readout that is closer to a stress gauge than discrete emotion labels
summary: Reward and punishment vectors are nearly antiparallel and work in models that never saw the maze, so RL recruits rather than creates the axis. A follow-up LessWrong post (Jhaveri et al., 'Desiderata for functional welfare experiments on LLMs', 2026-07-06) proposes inducing a low-welfare state with this vector and testing interventions, but reports no results.
found_by:
- search/intro-blog-scan-forums-affect
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
