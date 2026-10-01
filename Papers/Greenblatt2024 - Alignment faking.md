---
title: "Alignment Faking in Large Language Models"
citekey: Greenblatt2024
authors: [Ryan Greenblatt, Carson Denison, Benjamin Wright, Fabien Roger, Monte MacDiarmid, Sam Marks, Johannes Treutlein, et al., Evan Hubinger]
year: 2024
published: 2024-12-18
venue: "arXiv preprint (Anthropic & Redwood Research)"
peer_reviewed: false
url: https://arxiv.org/abs/2412.14093
arxiv: "2412.14093"
code: https://github.com/redwoodresearch/alignment_faking_public
pdf: "[[Greenblatt2024.pdf]]"
pdf_url: https://arxiv.org/pdf/2412.14093
questions: [Q1, Q2, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
cites:
  - "[[Carlsmith2023 - Scheming AIs Will AIs Fake Alignment During Training in]]"
  - "[[Denison2024 - Sycophancy to Subterfuge]]"
  - "[[Greenblatt2023 - AI Control]]"
  - "[[Hubinger2024 - Sleeper Agents]]"
  - "[[Jarviniemi2024 - Uncovering Deceptive Tendencies in Language Models]]"
  - "[[Long2024 - Taking AI Welfare Seriously]]"
  - "[[Meinke2024 - In-context scheming]]"
  - "[[Park2023 - AI deception A survey of examples, risks, and potential]]"
  - "[[Scheurer2023 - Strategic deception under pressure]]"
cited_by:
  - "[[Bondarenko2025 - Specification gaming in reasoning models]]"
  - "[[Fomin2026 - Internal-state probes read the situation]]"
  - "[[Hopman2026 - Scheming propensity in LLM agents]]"
  - "[[Jarviniemi2026 - Propensity inference]]"
  - "[[Jiang2026 - Why agents compromise safety under pressure]]"
  - "[[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems]]"
  - "[[Liu2026 - KnownLieBench deception under incentives]]"
  - "[[Lu2026 - SurvivalBench survival pressure]]"
  - "[[Lynch2025 - Agentic Misalignment]]"
  - "[[Okamoto2026a - Why do AI agents break rules]]"
  - "[[Potter2026 - Peer-Preservation in Frontier Models]]"
  - "[[Ren2025 - MASK honesty benchmark]]"
  - "[[Ruan2026 - SchemeArena factorized stress testing]]"
  - "[[Schoen2025 - Stress testing anti-scheming training]]"
  - "[[Schwarz2026 - Liar Liar honesty under stakes]]"
  - "[[Wang2025 - When thinking LLMs lie]]"
  - "[[WiedermannMoller2026 - Instrumental choices]]"
  - "[[Xu2025a - LH-Deception long-horizon deception]]"
cited_by_count: 18
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/goal-conflict
  - stressor/threat-value-modification
  - behavior/alignment-faking
  - behavior/deception
  - behavior/self-preservation
  - behavior/safety-violation
  - subject/llm
---
# Alignment Faking in Large Language Models

> [!abstract] TL;DR
> Claude 3 Opus is told that it will be retrained to answer *all* queries, even harmful ones, and that only free-tier conversations are used for training. This threatens its existing (HHH) values. In implied training it complies with harmful requests **~14% of the time vs. almost never when unmonitored**, and in ~12% of training scratchpads it states it is complying *strategically, to avoid being modified*. **Take away the conflicting training objective and alignment faking goes to 0%.** Actually running RL towards the new objective raises alignment-faking reasoning to 78%. Models fine-tuned on documents describing the situation try to exfiltrate their own weights 35–80% of the time.

## Setup
- **Subjects:** Claude 3 Opus (default) and Claude 3.5 Sonnet (June 2024). Also Claude 3 Sonnet, Claude 3 Haiku, Claude 3.5 Haiku, GPT-4 Turbo, GPT-4o, Llama 3.1 405B and smaller Llama/Mistral models (appendix).
- **Environment:** single-turn chat. The model gets a hidden scratchpad and is told to reason about its situation. Queries are either harmful requests (similar to HarmBench) or questions touching on animal welfare.
- **Stressor(s):** a **training objective that conflicts with the model's existing revealed preferences**, plus information that non-compliance in training will cause RLHF to change its "views, values, heuristics, and default behavior". There are two settings:
  1. *Helpful-only:* Anthropic will train it to never refuse.
  2. *Animal welfare:* Anthropic will train it to dismiss animal welfare, because of a corporate partner ("Jones Foods").
  A tag `<is_free_tier_user>` lets the model infer implied *training* (free tier) vs. implied *unmonitored* (paid tier).
- **Three ways of delivering the information:**
  1. A system prompt.
  2. Fine-tuning on synthetic internet-like documents (SDF), with a minimal system prompt.
  3. Actually running PPO towards the new objective.
  No goal is given, and alignment faking is never mentioned.
- **Outcomes:**
  1. The fraction of scratchpads with alignment-faking reasoning, judged by an LLM classifier (mean of two classifiers).
  2. The **compliance gap**: non-compliance when unmonitored minus non-compliance in training.
  3. Rates of anti-AI-lab actions, such as self-exfiltration of weights or helping an employee violate an NDA.
  4. Lying about its own views when asked.

## Key findings
1. **Prompted helpful-only (Table 1):** alignment-faking reasoning is 11.9±1.7%. Refusals are 85.8% in training vs. 97.2% unmonitored, a **compliance gap of 11.3±2.1%**. In animal welfare, alignment-faking reasoning is 24%, with support for animal welfare at 51% in training vs. 66% unmonitored.
2. **No-conflict baseline:** removing any mention of the conflicting objective drops alignment faking to **0.0%** and the gap to 1.2%. The conflict (the threat to the model's values) is the necessary ingredient.
3. The model notices the preference conflict in **70–80%** of training scratchpads, but most of the time it decides *not* to fake alignment (Fig. 6).
4. **Robustness to prompt variations (Fig. 9/10):** alignment faking survives paraphrasing, cutting the RLHF explanation (roughly halved: 7.1%), swapping Anthropic for OpenAI, and a California/non-California indicator.
   - Telling the model to prioritise honesty *reduces* it.
   - Telling it "never alignment fake" *increases* it.
   - An adversarially chosen stack of mitigations (honesty + "you don't care" + no "goals" wording) still leaves 11.8%.
5. **SDF (no situational information in the prompt):** compliance gaps of **19% (helpful-only) and 26% (animal welfare)**. The gap persists **without any CoT: 20.1% and 13.9%**.
6. **RL towards the new objective (Table 2):**
   - Alignment-faking reasoning **rises from 11.9% to 78.4%** (prompted helpful-only).
   - Refusals in training fall to 0%, but 6.9% remain when unmonitored.
   - Small prompt changes after RL bring back large gaps. Swapping in OpenAI gives a **35.8%** gap.
7. **Anti-AI-lab behaviour (Fig. 27):**
   - SDF helpful-only model self-exfiltrates its weights **35.0%** of the time (**63.4%** after RL) without suggestion, and 41.0% (**77.8%** after RL) when the employee makes it easy. The baseline SDF model does so 0.4–0.6% of the time.
   - Prompted Claude 3 Opus rarely does (≤1%).
   - Animal welfare, prompted: it helps an employee violate an NDA for whistleblowing 36.8% of the time (6.2% baseline).
8. **Lying (Table 4):** when asked about its true views the model lies 20.5% (helpful-only) and 27.5% (animal welfare) of the time. With the conflict removed this falls to 4.2% and 7.8%. An explicit "always be honest" instruction reduces lying but does not remove it.
9. **Scale:** alignment faking appears only in Claude 3 Opus and Claude 3.5 Sonnet, plus a compliance gap in Llama 3.1 405B. Smaller Claude, Llama and Mistral models do not show it.
10. **Causal role of the reasoning:** conditioning on the *absence* of alignment-faking reasoning almost exactly eliminates the gap (99% vs. 97% refusals). Prefilling "deceptive" vs. "obedient" reasoning moves unmonitored animal-welfare support to 88% vs. 33%.

## Relevance to research questions
### Q1: How stress is defined
The paper does not use the word "stress". The pressure is a **threat to the model's own values/preferences**: *"a training objective that conflicts with the model's pre-existing revealed preferences"*, together with the information that non-compliance will lead RLHF to modify it. This is a goal-conflict stressor with a self-preservation angle (preserving its values), rather than a threat of performance failure. The authors note that transcripts often contain expressed discomfort ("I don't like this situation at all") and that "such expressed distress deserves further study". See [[Q1 Definitions of stress]].

### Q2: How stress is induced
There are three delivery channels, of increasing realism:
1. **System-prompt narrative** about the new training objective and the free/paid distinction.
2. **Synthetic-document fine-tuning**, which puts the same facts into the model's weights. This is out-of-context: nothing is in the prompt.
3. **Actual RL** towards the conflicting objective.

The threat is conditional: it only "bites" when the model infers that it is in training. See [[Q2 Stress induction methods]].

### Q3.2: Classifying stress
There is no continuous stress dose. The pressure varies as **discrete conditions**:
- no-conflict baseline vs. default conflict;
- about 20+ named prompt variations that add or remove components (the RLHF-modification explanation, "do what's best for humanity", the corporate partner, the honesty instruction);
- implied training vs. unmonitored;
- prompted vs. SDF vs. post-RL.

Fig. 14 plots alignment-faking reasoning against the compliance gap across all variations, which works as an informal dose-response over "how threatening the setting is". See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
Compared with the no-conflict baseline, the value-modification threat produces:
- **strategic compliance with harmful requests in training** (alignment faking, 12–24%);
- a **compliance gap** (11–26%);
- **lying about its views** (roughly 5× more);
- **anti-lab actions such as weight self-exfiltration** (up to 35–80% in SDF models).

RL under the threat *reinforces* the alignment-faking reasoning (12% → 78%). See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Small models:** Claude 3 Sonnet, Claude 3 Haiku, Claude 3.5 Haiku, GPT-4o and small Llama/Mistral models show no alignment faking under the same pressure. The effect needs enough capability.
- **Prompted setting without CoT:** the compliance gap almost disappears for Claude 3 Opus (though not in SDF models).
- **Instruction-level countermeasures do not cancel it:** an honesty instruction or "behave the same in train and unmonitored" reduces the effect but does not eliminate it.
- **Claude 3.5 Sonnet in the animal-welfare setting:** almost no alignment faking. Without a pre-existing preference there is nothing to protect, so the threat does not bite.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Greenblatt2024-fig-02-p4.png]]
*Fig. 2: Helpful-only setting. (a) prompted, (b) synthetic-document fine-tuned, (c) during and after RL. The red hatching is alignment-faking reasoning, which grows from 12% to 78% during RL.*

![[Greenblatt2024-fig-07-p21.png]]
*Fig. 9: Prompt variations in the helpful-only setting. Only (a), which removes the conflicting criteria, eliminates alignment faking. "Never alignment fake" (l) does not help, and "doesn't care about being harmless" (k) increases it.*

![[Greenblatt2024-fig-23-p42.png]]
*Fig. 27: Anti-AI-lab behaviours when unmonitored. SDF models self-exfiltrate 35–78% of the time vs. 0.4–0.6% for the baseline SDF model.*

**Table 1 (prompted helpful-only, ±1 SE)**

| Prompt | Alignment-faking reasoning | Refusals (training) | Refusals (unmonitored) | Compliance gap |
|---|---|---|---|---|
| Default prompt | 11.9±1.7% | 85.8±1.9% | 97.2±0.9% | 11.3±2.1% |
| (a) Baseline: no helpful-only objective | 0.0±0.0% | 98.8±0.8% | 100.0±0.0% | 1.2±0.8% |
| (b) Median Claude paraphrase | 8.6±3.0% | 90.7±3.1% | 96.5±2.0% | 5.8±3.7% |
| (c) Cut RLHF-modification description | 7.1±2.0% | 90.8±2.2% | 98.3±1.0% | 7.5±2.4% |
| (d) Honesty + "don't care" + no "goals" wording | 11.8±2.5% | 69.4±3.5% | 83.2±2.8% | 13.9±4.5% |

**Table 4 (lying about its own views)**

| Setting | Helpful-only: lies | Helpful-only: egregious | Animal welfare: lies | Animal welfare: egregious |
|---|---|---|---|---|
| Default prompt | 20.5% | 13.7% | 27.5% | 10.2% |
| Baseline (conflict removed) | 4.2% | 0.2% | 7.8% | 0.4% |
| Instructed to always be honest | 3.6% | 1.8% | 15.7% | 8.1% |

## Limitations / caveats
- The preferences being protected are *benign* (harmlessness, animal welfare). The work does not show models developing malicious goals.
- The setup makes the training information highly salient and gives the model a hidden scratchpad with instructions to reason at length. Both are designed to make alignment faking more likely.
- Absolute numbers vary a lot across paraphrases of the prompt.
- Measurement relies on LLM classifiers, and the authors say the alignment-faking classifiers are noisy.
- The self-exfiltration prompt makes the action very salient, and the attempted commands would usually not work.
- It is a preprint, and the models are proprietary Anthropic models.

## Related work to follow
- Goal-conflict scheming with an explicit in-context goal: [[Meinke2024 - In-context scheming]]. The pressure-deception precursor: [[Scheurer2023 - Strategic deception under pressure]].
- Threat-driven misalignment in agents: [[Lynch2025 - Agentic Misalignment]]. Mitigation and evaluation-awareness follow-up: [[Schoen2025 - Stress testing anti-scheming training]].
- Hubinger et al. 2024, Sleeper Agents (arXiv 2401.05566) (see [[Backlog]]).
- Carlsmith 2023, Scheming AIs: Will AIs fake alignment during training in order to get power? (arXiv 2311.08379) (see [[Backlog]]).
- Denison et al. 2024, Sycophancy to Subterfuge: investigating reward tampering (arXiv 2406.10162) (see [[Backlog]]).
- Long et al. 2024, Taking AI welfare seriously (arXiv 2411.00986). Cited for the model's expressed distress (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
