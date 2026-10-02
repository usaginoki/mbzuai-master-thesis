---
title: Retrying vs Resampling in AI Control
citekey: Lucassen2026
authors: Lucassen & Kaufman 2026
year: 2026
published: 2026-05-25
venue: arXiv preprint
url: https://arxiv.org/abs/2605.26047
arxiv: '2605.26047'
pdf_url: https://arxiv.org/pdf/2605.26047
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q17.2
status: candidate
priority: 2
relevance: core
manipulation: Maximum monitor suspicion over five samples drawn from the same context per step (untrusted Claude Opus 4.6, trusted MiMo-V2-Flash, BashArena)
outcome: Attack steps before execution; safety rises from 61% to 71% at 0.3% audit budget; selective resampling recovers 6.2 pp with 10% of the extra samples
timing: pre-action
why: 'Updates Ctrl-Z: resampling works as a predictive signal (max, not min) rather than as an action-substitution mechanism; retrying leaks monitor rationale.'
summary: Retrying (blocking and continuing) lets the untrusted model exploit monitor rationale and negates safety gains. Resampling five times and auditing on the maximum suspicion raises safety from 61% to 71% at a 0.3% audit budget at no usefulness cost. Contrary to Ctrl-Z, max beats min for auditing and executing the least suspicious sample adds only +3.9 pp with a confidence interval overlapping zero.
found_by:
- search/pred-self-and-cross-model
- search/a2a-effects-safety
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
