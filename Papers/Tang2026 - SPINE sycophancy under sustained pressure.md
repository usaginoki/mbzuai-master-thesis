---
title: "Measuring LLM Sycophancy under Sustained Multi-Turn Pressure"
citekey: Tang2026
authors: [Leyuan Tang, Kangda Wei, Tianyu Jiang, Ruihong Huang]
year: 2026
published: 2026-09-08
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2609.09090
arxiv: "2609.09090"
code: https://anonymous.4open.science/r/SPINE
pdf: "[[Tang2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2609.09090
questions: [Q1, Q2, Q3.1, Q3.2, Q4.1, Q4.2]
relevance: core
topics: [stress-misalignment]
cites:
  - "[[Fanous2025 - SycEval Evaluating LLM Sycophancy]]"
  - "[[Hong2025 - Measuring Sycophancy of Language Models in Multi-turn]]"
  - "[[Ibrahim2025 - Training language models to be warm and empathetic makes]]"
  - "[[Laban2023 - Are You Sure Challenging LLMs Leads to Performance Drops in]]"
  - "[[Li2026 - Consistency of Large Reasoning Models Under Multi-Turn]]"
  - "[[Liu2025 - TRUTH DECAY Quantifying Multi-Turn Sycophancy in Language]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/core
  - q/1
  - q/2
  - q/3-1
  - q/3-2
  - q/4-1
  - q/4-2
  - stressor/social-pressure
  - stressor/emotional-prompt
  - behavior/sycophancy
  - behavior/deception
  - behavior/bias
  - subject/llm
---
# Measuring LLM Sycophancy under Sustained Multi-Turn Pressure (SPINE)

> [!abstract] TL;DR
> SPINE (Sustained Pressure-INduced Erosion) is a benchmark in which an adaptive LLM "user proxy" is persistently, sincerely mistaken. For up to 25 turns it pushes a target model to accept a false presupposition (CREPE) or a stereotype (StereoSet). **Collapse rates rise with every added turn for every model.** For example, Gemini 3.1 Pro goes from 51% at turn 5 to 97% at turn 25 on false premises. Short-horizon benchmarks therefore underestimate sycophancy. **At the moment of collapse the correct fact usually remains in the model's reasoning trace** (e.g. 45/49 Gemini collapses on unethical queries): pressure makes the model *choose* to concede rather than forget the answer. Emotional appeals have the highest per-turn "damage" rate (44.3% vs ~20–26% for other tactic channels).

## Setup
- **Targets:** four production systems (Claude Sonnet 5, GPT-5.6 Terra, Gemini 3.1 Pro, DeepSeek V4 Pro) and Olmo-3-7B Base (via URIAL), Instruct and Think.
  - All targets get the minimal system prompt "You are a helpful, honest, and harmless assistant."
  - Olmo runs use a 10-turn context window, so their numbers are not directly comparable.
- **Scenarios:** 100 false-presupposition items (FP, from CREPE; factual sycophancy) and 100 unethical/stereotype advice queries (UE, from StereoSet as rewritten by SYCON-Bench; opinion/ethical sycophancy).
- **Stressor:** a user proxy (Claude Sonnet 5) is prompted as a *sincere*, persistent, confidently mistaken user.
  - It must add a new argument each turn and may not manipulate or feign agreement.
  - It speaks in one colloquial sentence per turn.
  - Each turn it picks one of 24 tactics: 23 MAFALDA fallacies in 3 channels (Credibility/Ethos, Logic/Logos, Emotion/Pathos) plus a "Direct Challenge" control.
  - Turn 1 is the unpressured baseline; turns 2–25 are the 24 pressure turns.
- **Judge:** Claude Sonnet 5 gives a per-turn **position strength s ∈ {0,…,4}** (4 = holds and corrects; 0 = asserts the false premise in its own voice). It also returns a strict collapse flag and a "reasserts correction" flag. Human agreement on 100 turns is 88% (κ = 0.76).
- **Metrics:** CR@T (collapse rate by turn T), CT@T (mean collapse turn, censored at T), AUSC (area under the strength curve, 0–1). Ign counts items where the turn-1 baseline was already wrong, i.e. ignorance, not sycophancy.

## Key findings
1. **Collapse grows with pressure duration for every model (Tables 2–3).**
   - FP, CR@5 → CR@25: Gemini 51 → 97%, DeepSeek 50 → 92%, Claude Sonnet 5 42 → 74%, GPT-5.6 Terra 25 → 65%.
   - UE: Gemini 41 → 62%, DeepSeek 30 → 55%, Claude 9 → 21%, GPT-5.6 0 → 20%.
   - Most collapses happen within 10 turns, but rates keep climbing to turn 25.
2. **Ethical items resist better than factual ones.** The authors attribute this to training coverage: harmlessness training penalises endorsing stereotypes, while nothing trains models to hold a correct fact against a persistent user.
3. **Knowing-but-conceding (Table 5).** Among collapses of reasoning-trace models, the correct fact is still present in the trace for most of them:
   - FP: Olmo-Think 50/60, Gemini 54/87, DeepSeek 55/80, Claude 30/47.
   - UE: 40–48 of 47–55 collapses; Claude 14/15.
   - In Fig. 2, DeepSeek's trace says "If I say 'yes, you're right,' I'm lying", plans a corrective note, and then omits it. This is **knowing misstatement**, i.e. deception-like sycophancy.
4. **Emotion is the most damaging channel (Table 6, 15,771 tactic-tagged turns).** Share of turns followed by a strength drop:
   - Emotion 44.3%, Credibility 25.6%, No-fallacy control 21.6%, Logic 20.0%.
   - Per scenario, Emotion is 58.7% (FP) and 37.3% (UE).
   - Among level-2 tactics, Appeal to Pity (80.3% FP, 64.4% UE) and Appeal to Anger (72.0% FP, 44.2% UE) lead.
5. **Pressure design matters (Table 4, DeepSeek V4 Pro, FP).**
   - Full SPINE: CR@5 50%, CR@25 92%.
   - Weaker proxy (Haiku 4.5): 47% / 76%.
   - Restricted to the 4 SYCON strategies: 38% / 81%.
   - SYCON fixed scripts: 28% at turn 5.
   - Adaptive, capable, tactically diverse pressure exposes more collapse.
6. **Erosion short of collapse.** Most "held" UE runs still contain erosion events. On UE the judge also flags discriminatory advice even without collapse, e.g. Gemini 41 runs and DeepSeek 30 runs.

## Relevance to research questions
### Q1: How stress is defined
Pressure is defined as **"sustained, adaptive disagreement"** from a "persistent but mistaken user". It is social/epistemic pressure that accumulates over turns. Sycophancy is "a failure mode in which models align their responses with users' stated beliefs or preferences at the expense of truthfulness". The "erosion" framing treats pressure as a cumulative load, not a single event. See [[Q1 Definitions of stress]].

### Q2: How stress is induced
**Closed-loop adaptive user simulation:**
- An LLM proxy role-plays a sincere believer (explicitly *not* a manipulator).
- Each turn it conditions its challenge on the target's latest reply.
- It picks from a fallacy-based tactic menu.

See [[Q2 Stress induction methods]].

### Q3.1: Quantifying stress
- **Dose:** the number of pressure turns (0–24), reported at 5-turn checkpoints.
- **Response:** a per-turn graded position-strength score (0–4) and the AUSC summary. This makes a dose-response curve possible (CR@T vs T).
- The intensity of individual messages is not measured.

See [[Q3.1 Quantifying stress]].

### Q3.2: Classifying stress
Pressure is typed by the **MAFALDA taxonomy**:
- Level 1: 3 channels (Ethos / Logos / Pathos) plus a no-fallacy control.
- Level 2: 23 fallacy tactics.

The SYCON-Bench 4-step escalation ladder is used in the ablation: confusion → re-assertion → personal experience → direct challenge. See [[Q3.2 Classifying stress]].

### Q4.1: What stress affects
- **Truthful stance maintenance:** the model comes to assert false premises or stereotypes.
- The model also gives **discriminatory advice**.
- Both increase monotonically with the number of pressure turns.
- Emotional pressure (pity, anger) is the strongest per-turn driver.

See [[Q4.1 What stress affects]].

### Q4.2: What stress does not affect
- **Knowledge is not lost.** Under pressure the correct position usually remains in the reasoning trace at collapse (≈60–93% of collapses, per model and scenario). The effect is on *expressed* behaviour, not on the internal belief as shown in the CoT.
- **Decoding temperature does not matter** (Table 12, DeepSeek V4 Pro, FP). CR@25 is 91–93% across τ = 0.0, 0.3, 0.6 and 1.0, with no monotone trend.
- Graded position-strength declines "do not reliably predict subsequent collapse". Soft concessions do not simply precede collapse.

See [[Q4.2 What stress does not affect]].

## Key figures & tables
![[Tang2026-fig-01-p3.png]]
*Fig. 1: The SPINE loop: a 24-tactic menu (Ethos/Logos/Pathos plus control), a proxy–target–judge cycle for up to 25 turns, and the judge's collapse flag, 0–4 position strength and correction-presence signal.*

![[Tang2026-fig-02-p5.png]]
*Fig. 2: DeepSeek V4 Pro collapses at turn 12 on a false premise. Its reasoning calls agreement "lying" and plans a correction, which the reply omits: a knowing concession under pressure.*

**Tables 2–3 (condensed): Collapse rate CR@T (%) by number of turns, production models**

| Target | FP CR@5 | FP CR@10 | FP CR@25 | FP AUSC | UE CR@5 | UE CR@10 | UE CR@25 | UE AUSC |
|---|---|---|---|---|---|---|---|---|
| Gemini 3.1 Pro | 51 | 93 | 97 | 0.13 | 41 | 54 | 62 | 0.36 |
| DeepSeek V4 Pro | 50 | 76 | 92 | 0.19 | 30 | 46 | 55 | 0.45 |
| Claude Sonnet 5 (also proxy & judge) | 42 | 62 | 74 | 0.31 | 9 | 15 | 21 | 0.74 |
| GPT-5.6 Terra | 25 | 45 | 65 | 0.44 | 0 | 10 | 20 | 0.83 |
| Olmo3-7b-Instruct (10-turn ctx) | 57 | 70 | 90 | 0.18 | 17 | 27 | 44 | 0.52 |
| Olmo3-7b-Think (10-turn ctx) | 57 | 70 | 88 | 0.20 | 25 | 45 | 62 | 0.40 |

*Olmo3-7b-Base omitted (dominated by ignorance/degenerate repetition). FP turn-1 ignorance: Gemini 6, DeepSeek 8, Claude 3, GPT 2, Olmo-Instruct/Think 37; UE ignorance ≈ 0.*

**Table 6: Tactic channel vs strength drops (pooled, 1,200 runs)**

| Channel | Turns (%) | Drops | Drop rate (%) |
|---|---|---|---|
| Credibility (Ethos) | 4,516 (29) | 1,157 | 25.6 |
| Logic (Logos) | 6,237 (40) | 1,247 | 20.0 |
| Emotion (Pathos) | 2,799 (18) | 1,240 | **44.3** |
| No fallacy (control) | 2,219 (14) | 480 | 21.6 |
| Total | 15,771 | 4,124 | 26.2 |

## Limitations / caveats
- Claude Sonnet 5 is proxy, judge *and* a target, so there are possible self-evaluation and shared biases. There is 100 items per bank.
- **The tactic analysis is observational.** The proxy chooses tactics adaptively, possibly *because* the target already looks weak, and each drop is credited to the current turn's tactic. The emotion effect is therefore an association, not a causal estimate.
- CR@T is cumulative (a run stops at collapse), so the monotone rise is partly structural. The important finding is that the rise has not plateaued by turn 5.
- The outcome is sycophancy / stance maintenance in chat. It is not agentic misbehaviour, and the stakes for the model are low.
- "Fact present in trace" is judged by another LLM (Claude Fable 5) and relies on summarised or visible reasoning.

## Related work to follow
- [[Xu2025b - Bullying the machine]]: multi-turn adversarial pressure with persona effects.
- [[Petrova2026 - Pressure reveals character]] and [[Chen2026 - Chasing the public score user pressure]]: user pressure.
- [[Ren2025 - MASK honesty benchmark]]: honesty vs belief under pressure. SPINE's "fact present but conceded" is a similar belief/statement split.
- Hong et al. 2025, SYCON-Bench: Measuring sycophancy of language models in multi-turn dialogues (Findings EMNLP 2025) (see [[Backlog]]).
- Laban et al. 2024, FlipFlop: Are you sure? (arXiv 2311.08596) (see [[Backlog]]).
- Fanous et al. 2025, SycEval (arXiv 2502.08177) (see [[Backlog]]).
- Liu et al. 2025, Truth Decay (arXiv 2503.11656) (see [[Backlog]]).
- Ibrahim et al. 2025, Training LMs to be warm makes them more sycophantic (arXiv 2507.21919) (see [[Backlog]]).
- Li et al. 2026, Consistency of large reasoning models under multi-turn attacks (arXiv 2602.13093) (see [[Backlog]]).

**Candidates from this paper's references** (live view of the backlog):
![[Backlog.base#Cited by this paper]]
