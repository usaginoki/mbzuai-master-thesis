---
title: 'SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do'
citekey: Dhodapkar2026
authors: Dhodapkar and Pishori 2026
year: 2026
published: 2026-03-28
venue: arXiv preprint
url: https://arxiv.org/abs/2603.27148
arxiv: '2603.27148'
pdf_url: https://arxiv.org/pdf/2603.27148
topics:
- misalignment-prediction
status: candidate
priority: 1
relevance: core
manipulation: Sequence of abstract safety states of a trajectory; absorbing Markov chain with closed-form finite-horizon absorption probability
outcome: Probability of reaching a violation within k steps; detects 94.7% of violations with 3.7 steps of advance warning vs 52.6% for per-step LLM judges
timing: earlier-in-trajectory
why: A head-to-head of a cheap predictive monitor against a reactive per-step LLM judge, with lead time reported.
summary: 'Targets ''safety drift'', where individually safe steps (read confidential file, summarise, email externally) compound into a violation. On 357 traces over 40 tasks, points of no return are strongly task dependent: in communication tasks a mild-risk state implies an 85% chance of violation within five steps, in technical tasks under 5% from any state. The monitor beats keyword matching (44.7% detection, 55.9% FPR) and per-step LLM judges (52.6% detection, 38.2% FPR) and runs over 60,000x faster; small two-author study, and the monotone state design makes eventual violation certain by construction.'
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
