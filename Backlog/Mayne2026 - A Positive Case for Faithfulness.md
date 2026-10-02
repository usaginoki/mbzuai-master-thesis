---
title: 'A Positive Case for Faithfulness: LLM Self-Explanations Help Predict Model Behavior'
citekey: Mayne2026
authors: Mayne et al. 2026
year: 2026
published: 2026-02-02
venue: arXiv preprint
url: https://arxiv.org/abs/2602.02639
arxiv: '2602.02639'
pdf_url: https://arxiv.org/pdf/2602.02639
topics:
- misalignment-prediction
status: candidate
priority: 2
relevance: adjacent
manipulation: Model's self-explanation of a decision, given to an observer who then predicts the model's behaviour on counterfactual inputs (Normalized Simulatability Gain)
outcome: Model decisions on 7,000 counterfactuals (health, business, ethics) for 18 models; self-explanations give 11-37% NSG and beat explanations from external, even stronger, models; 5-15% are egregiously misleading
timing: pre-generation
why: Quantifies how much a model's own words help a third party predict its future outputs, and the rate at which they mislead.
summary: NSG measures how much an explanation improves an observer's prediction of the model on related inputs. Across 18 frontier models self-explanations improve prediction by 11-37% NSG and carry more predictive information than explanations from external models, which the authors attribute to self-knowledge. Between 5% and 15% of self-explanations are egregiously misleading.
found_by:
- search/pred-self-and-cross-model
cited_by: []
cited_by_count: 0
added: 2026-10-01
tags:
- type/candidate
---
