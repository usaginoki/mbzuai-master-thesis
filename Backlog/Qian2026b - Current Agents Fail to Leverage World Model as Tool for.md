---
title: Current Agents Fail to Leverage World Model as Tool for Foresight
citekey: Qian2026b
authors: Qian et al. 2026
year: 2026
published: 2026-01-07
venue: arXiv preprint
url: https://arxiv.org/abs/2601.03905
arxiv: '2601.03905'
pdf_url: https://arxiv.org/pdf/2601.03905
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: VLM agents given a generative world model as an optional simulation tool
outcome: 'Not a safety predictor: measures whether agents use and benefit from simulated futures; simulation invoked in fewer than 1% of cases, misread about 15% of the time, performance drops up to 5%'
timing: pre-action
why: 'Counter-evidence: handing an agent a simulator does not give it foresight, which argues for an external monitor doing the look-ahead.'
summary: Across agentic and VQA tasks, agents rarely call the world model, misinterpret its predictions, and sometimes do worse with it. The authors attribute this to not knowing when to simulate, how to interpret rollouts, and how to integrate them.
found_by:
- search/pred-preexecution-lookahead
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
