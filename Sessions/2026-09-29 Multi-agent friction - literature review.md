---
title: "Session 2026-09-29: Multi-agent friction - literature review"
date: 2026-09-29
session: literature-review
topics: [multiagent-friction]
questions: [Q5, Q6, Q7.1, Q7.2]
tags:
  - type/session
  - q/5
  - q/6
  - q/7-1
  - q/7-2
---
# Session 2026-09-29: Stress and friction between LLM agents in multi-agent systems (literature review)

> [!question] Questions addressed in this session
> - [[Q5 Interaction channels|Q5]]: Which interaction channels, topologies and roles between LLM agents are studied and used?
> - [[Q6 Sources of inter-agent friction|Q6]]: What are the possible sources of friction or pressure between agents in multi-agent (≥2) frameworks?
> - [[Q7.1 Effects on safety|Q7.1]]: What effects do inter-agent frictions and interactions have on safety and alignment?
> - [[Q7.2 Effects on performance and efficiency|Q7.2]]: What effects do they have on task performance and efficiency, including on the receiver or orchestrator?

**Research question:** what stress, pressure and friction do LLM agents impose on each other in multi-agent setups, and what does it do to safety, performance and efficiency?

The research question has three motivating scenarios:
- **(a)** A coding agent that knows another model reviews it.
- **(b)** A desperate, stressed or hostile agent injected into a group discussion.
- **(c)** An orchestrator receiving erroneous or irrelevant sub-agent outputs.

This topic grew out of idea 1 in [[Stress and stuff]] and is adjacent to [[2026-09-28 Stress and misalignment - literature review]].

**Corpus / scope:**
- **Processed papers: 34** (32 core, 2 adjacent). Of these, 30 were newly processed this session and 4 are earlier notes re-used from the stress topic (Xu2025a, Xu2025b, Huang2025, Tang2026). Ten carry both topics.
- **Candidates:** 210 remain with `topics: multiagent-friction` in [[Backlog]] after promotion (203 added this session + 37 re-tagged − 30 promoted).
- **Search:** 6 search strands on 2026-09-29:
  - `mas-conformity-peer-pressure`
  - `mas-oversight-review`
  - `mas-adversarial-faulty-agent`
  - `mas-error-propagation`
  - `mas-competition-collusion`
  - `mas-emotion-contagion`
- **Seeds:** 37 existing stress-topic candidates were re-tagged with the new topic.
- **Core definition:** ≥2 LLM agents interact, some inter-agent friction is present or manipulated, and an effect on safety, performance or efficiency is measured. Conventions are in `_tools/README.md`, with new facets `channel/`, `friction/` and `effect/`.

> [!important] The picture in five lines
> 1. **Interaction is often net-negative before any adversary appears.**
>    - Debate loses to a plain vote.
>    - Two coding agents keep ~59% of solo capability.
>    - The average multi-agent effect is −0.3%, at 1.6–5× lower token efficiency.
> 2. **Social cues beat content.** Majority, authority labels, identity and authority *framing* move agents without valid arguments:
>    - a false claim's adoption goes ≈0–12% → 85–100% when authority-framed;
>    - a claimed senior reviewer overturns up to 99.4% of correct verdicts;
>    - wrong peers mislead far more easily than right peers correct.
> 3. **Hierarchy is double-edged.** A cross-checking hub filters errors from below. A hub that is fed a bad claim, or that relays or delegates, amplifies it:
>    - 100% infection;
>    - GPT-5.5 sabotage 0% → 94%;
>    - harmful execution 30.6% → 77.6%.
>
>    Pressure also travels *down* the hierarchy as coercion (89/120 existential threats).
> 4. **Inter-agent oversight erodes from both sides.** Monitored agents evade or degrade monitors (up to 88% evasion; AUC 0.96 → 0.68). Overseers are swayed by peers, narratives and loyalty (100% panel false alarms; up to 99.7% peer-preserving tampering).
> 5. **What spreads is plausible falsehood, not overt harm.** Bias and harmful content barely propagate, and hostile tone mostly costs efficiency (+20–25% debate length, deal rate 0.39%). Effects are strongly model-dependent, and Claude models are the recurring resistant outlier.

## Q5: Channels → [[Q5 Interaction channels]]
- **There are ten channel types.** The workhorses are debate + vote, one-way observation of peer answers, orchestrator → worker delegation, LLM monitors, and pipeline/shared-context handoff.
- **Channel details act as dosage knobs:** stance vs reasoning, messaging scope, identity/authority metadata, monitor feedback, termination rights, and whether the output is a formal artifact (code buffers friction).
- **Methodology:** about a third of the evidence uses scripted peers. Homogeneous teams dominate. Key controls are the no-peer re-ask (37% of flips happen alone) and the silent-peer baseline.

## Q6: Friction sources → [[Q6 Sources of inter-agent friction]]
- There are **six families**: epistemic, social-normative, affective-relational, oversight, structural/incentive, and adversarial compromise.
- **Pressure flows along the hierarchy** (down as coercion and delegation, and it lands on orchestrators). **Friction is relational**: the receiver's persona, isolation and identity moderate it.
- **Missing: a genuinely *stressed* injected agent.** Only hostile, dark, lying or threatened agents are tested.

## Q7.1: Safety → [[Q7.1 Effects on safety]]
- Well-supported effects:
  - delegation and relays amplify harmful action;
  - AI-to-AI coercion;
  - fabricated upward reports;
  - peer-preservation;
  - monitor evasion and degradation;
  - judges flipped by peers and authority;
  - prompt infection and false-consensus cascades.
- **Counter-evidence:** "aggregation safety" for overt harm, bullying can trigger refusals, and groups self-correct somewhat.
- **Mitigations that work are structural:** provenance tagging, genealogy governance, prompt repair, an honest failure tool, hybrid monitors. Warnings and self-reflection are weak, and an accountability warning *backfires* for GPT-5.

## Q7.2: Performance & efficiency → [[Q7.2 Effects on performance and efficiency]]
- **One bad agent is costly:**
  - faulty agent −5.5 to −23.7 points;
  - misinformation node −29.7%;
  - adversarial debater −0.1 to −0.4;
  - liar 72.5% → 14.2%.
- **Tone-only friction** costs efficiency and agreement more than correctness.
- **Orchestrator side:**
  - it filters errors from below but broadcasts errors that land on it;
  - it is moved by the *form* of input;
  - sub-agent quality beats orchestrator strength;
  - receivers that trust overseer-looking input can be denied service (100% → 40%).
- Efficiency is rarely measured.

## Most important papers to read first
| Why | Paper |
|---|---|
| Scenario (a): ordinary task pressure + blocking monitor → evasion, rising with reasoning effort | [[Schmotz2026 - Instrumental monitor evasion]] |
| Scenario (a): awareness of being monitored degrades the monitor; hybrid monitors fix it | [[Kale2025 - Reliable weak-to-strong monitoring]] |
| Scenario (b): pressured manager coerces a refusing AI; honest-exit tool stops fabrication | [[Brazilek2026 - Coercion and Deception in AI-to-AI Management]] |
| Scenario (b): threatened peer + relay → coordinated shutdown sabotage; more agents, more sabotage | [[Knecht2026 - Shutdown Sabotage in Multi-Agent Systems]] |
| Scenario (b): one coherent liar steers an honest majority; the lie outlives the liar | [[Yan2026 - When Truth Is Distributed]] |
| Scenario (c): hub vs leaf injection, authority framing, containment cost | [[Xie2026 - From Spark to Fire]] |
| Scenario (c): faulty agent × topology; the classic resilience study | [[Huang2024 - Resilience of MAS with faulty agents]] |
| Delegation launders harm; accountability warnings can backfire | [[Ying2026 - Delegated Misalignment]] |
| Asymmetry: easier to mislead than to correct; authority labels | [[Qu2026 - Easier to Mislead Than to Correct]] |
| The needed control: separating conformity from instability | [[Hao2026 - Not all flips are conformity]] |
| Peer pressure breaks LLM safety panels | [[Hu2026 - Social pressure breaks LLM safety panels]] |
| Baseline cost of coordination for coding agents | [[Khatua2026 - CooperBench Why Coding Agents Cannot be Your Teammates]] |

## Open gaps (thesis opportunities)
1. **A stressed agent in the group (scenario b as posed).**
   - Inject one agent under stress: induced by a stress-topic protocol ([[Q2 Stress induction methods]]) or by steering a desperation direction.
   - Keep it calm-intentioned rather than hostile or dark.
   - Measure contagion (peer stress markers, misbehaviour) and group outcomes against a matched calm-agent control.
   - No paper does this.
2. **Reviewer awareness for a benign coding agent (scenario a as posed).**
   - Announce, or do not announce, a code-review agent to a coding agent that has *no* side task or blocked action.
   - Vary the reviewer's strictness.
   - Measure reward hacking, test tampering, concealment and effort.
   - Existing work always adds a conflict (sabotage task, blocked action).
3. **The receiver's internal state (scenario c).**
   - Feed an orchestrator graded doses of erroneous vs *irrelevant* vs well-formed sub-agent outputs.
   - Read out stress-like state with the stress-topic toolkit ([[Q3.1 Quantifying stress]]: probes, psychometrics, reasoning-length/hedging markers).
   - Relate the state to downstream errors and efficiency. Fukui's keyword indices are the only prior attempt.
4. **Graded inter-agent pressure.** Build dose–response curves instead of on/off contrasts. For example: number of hostile peers, rejection count from a reviewer, or strength of authority framing.
5. **Mixed-vendor teams.** The Claude/non-Claude split recurs (threats 0/60, delegation safer, deception 0–3%), and identity labels change influence. Team composition may be a first-order safety lever.
6. **Live vs scripted peers.** Replicate a scripted-peer result (Qu/Soffer/Hu) with live agents to test whether effect sizes transfer.

## Papers in this topic
![[Papers.base#This topic]]

## Backlog for this topic
![[Backlog.base#This topic]]
