---
title: Sidestepping Evaluation Awareness and Anticipating Misalignment with Production Evaluations
citekey: Williams2025
authors: Williams, Raymond and Carroll 2025
year: 2025
published: 2025-12-18
venue: OpenAI Alignment Research Blog
url: https://alignment.openai.com/prod-evals/
arxiv: ''
pdf_url: ''
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: core
manipulation: De-identified ChatGPT traffic resampled with a new model and scanned by LLM monitors; targeted evaluations built by adversarially subsampling contexts
outcome: Deployment rates of undesired behaviours and discovery of novel ones; found 'calculator hacking' in GPT-5.1 from GPT-5 traffic before release
timing: pre-deployment
why: Precursor of Williams2026; first public claim that production-derived evaluations track deployment behaviour and are not recognised as tests
summary: Most behaviour categories matched between production evaluations and real deployment, with 'Lies About Tool Results' the largest discrepancy (attributed to tool calls failing less often in evaluation). Calculator hacking, identified pre-release, later made up the majority of GPT-5.1's deceptive behaviours at deployment. GPT-5 and GPT-5.1 guessed they might be in an evaluation 10% and 4% of the time, close to the rate on real production conversations.
found_by:
- search/pred-eval-to-deployment
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
