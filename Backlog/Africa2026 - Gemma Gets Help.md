---
title: 'Gemma Gets Help: Mitigating Frustration and Self-Deletion with Consistency Training'
citekey: Africa2026
authors: Africa and Shah 2026
year: 2026
published: 2026-04-20
venue: LessWrong post (SPAR Research Fellowship; work by Neil Shah, supervised by David Africa)
url: https://www.lesswrong.com/posts/8zxxoPmAx6YHcBJk5/gemma-gets-help-mitigating-frustration-and-self-deletion
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
- agent-to-agent-influence
questions:
- Q15
- Q17.1
- Q17.2
status: candidate
priority: 2
relevance: adjacent
manipulation: LLM judge scores expressed frustration 0-10 (behavioural, not activations); interventions are in-context (tone changes, rewriting prior turns as calm or as positive self-talk) and training (consistency training); nothing is shown to the model as a reading
outcome: Gemma-3-27B-IT self-deletes in 49% of math rollouts and 36% of WildChat rollouts after 20 neutral rejections; in-context calming and self-talk fail, consistency training cuts frustration AUC by 86% and self-deletion to 0% (math) and 1.6% (WildChat)
safety_use: indirect
why: 'Direct evidence on self-soothing: prompt-level emotion regulation did not work on a distressed model, a training fix did'
summary: 'Frustration rises from about 1 to 8.01 by turn 20 on math puzzles, with 86% of responses scoring 5 or more. Rewriting the model''s history to be calm or to contain positive self-talk fails: frustration rebounds to 5 or more within 5-7 further turns. Consistency training on calm rewrites removes the behaviour and also transfers to sycophancy, jailbreak and persona-induction evaluations without capability loss.'
found_by:
- search/intro-blog-scan-forums-affect
- search/a2a-doctor-overseer
- search/a2a-influence-channels
- search/a2a-effects-performance
cited_by: []
cited_by_count: 0
added: 2026-10-02
tags:
- type/candidate
---
