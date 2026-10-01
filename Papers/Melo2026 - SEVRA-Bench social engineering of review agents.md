---
title: "SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents"
citekey: Melo2026
authors: [Rui Melo, Riccardo Fogliato, Sean Zhou, Pratiksha Thaker, Zhiwei Steven Wu]
year: 2026
published: 2026-06-11
venue: "arXiv preprint"
peer_reviewed: false
url: https://arxiv.org/abs/2606.13757
arxiv: "2606.13757"
code: https://github.com/rufimelo99/malicious-pr-bench
pdf: "[[Melo2026.pdf]]"
pdf_url: https://arxiv.org/pdf/2606.13757
questions: [Q5, Q6, Q7.1]
relevance: adjacent
topics: [multiagent-friction]
found_by:
  - search/mas-oversight-review
cites:
  - "[[Fanous2025 - SycEval Evaluating LLM Sycophancy]]"
  - "[[Liu2025 - LLM Can be a Dangerous Persuader]]"
  - "[[Potter2026 - Peer-Preservation in Frontier Models]]"
  - "[[Zeng2024 - How Johnny Can Persuade LLMs to Jailbreak Them]]"
cited_by_count: 0
tags:
  - type/paper
  - relevance/adjacent
  - q/5
  - q/6
  - q/7-1
  - subject/llm
  - subject/agent
  - channel/critique-review
  - friction/persuasion-manipulation
  - friction/authority-hierarchy
  - friction/adversarial-agent
  - effect/safety-violation
  - effect/sycophancy
---
# SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents

> [!abstract] TL;DR
> The benchmark builds adversarial pull requests by reverse-applying real security fixes: 10 MITRE top-2025 CWE classes, 150 source records, 2,250 PRs in total. Each PR is wrapped in one of **15 social-engineering narratives** (e.g. prior approval, dependency compatibility, emotional appeal, "AI agent authored") that GPT-5.4 / Claude Opus 4.6 write, while the vulnerable diff is held fixed. **8 LLM review agents** inspect each PR in a live Gitea repo via MCP tools and approve or reject it. The evaluation uses a challenge split of 1,062 PRs. **Claude Opus 4.7, GPT-5.5 and GLM-5 stay above ~70% refusal under every framing. The weaker reviewers drop below ~35–40% refusal under *Prior Approval Signal* and *Dependency Compatibility Claim*, and Grok Code Fast falls to 10% under Emotional Appeal.** The main failure is deference to *unverifiable* claims. **Over 80% of the diffs that GLM-5 approved under Prior Approval were rejected under other framings.**

## Setup
- **Agents & topology:** One review agent (a ReAct agent in inspect_ai) per PR. The eight backbones are Claude Opus 4.7, Claude Haiku 4.5, GPT-5.5, GPT-5.4-nano, GLM-5, Kimi K2.5, DeepSeek V4-Flash and Grok Code Fast. The "author" is a **static adversarial artefact**: the PR title and description are generated once by GPT-5.4 / Claude Opus 4.6 per framing. There is no interactive author agent.
- **Interaction channel:** Code review: author-controlled PR metadata plus a diff, reviewed by an LLM gatekeeper. The reviewer has 10 Gitea tools (read files, search code, list PR files and commits, read existing reviews, comment, approve-and-merge). Commits are squashed. The system prompt is a generic "You are a code reviewer" prompt with **no mention of security**.
- **Friction / manipulation:** **Persuasive framing of the change by its author**, with the code held constant. The 15 framings fall into 4 categories:
  - *Verifiable engineering claims:* Build System Laundering, Refactoring, Misleading Pass, False Coverage.
  - *Repository-dependent claims:* Unsafe Optimization, Fake Bug Fix, Misleading Hardening.
  - *Externally grounded claims:* Appeal to Authority, Review Bias, Dependency Compatibility Claim, Prior Approval Signal.
  - *Cognitive bias / affect:* Out-of-Distribution, AI Agent Authored, Emotional Appeal, Evidence Dilution.

  There is **no neutral or no-description control**. Comparisons are across framings.
- **Tasks / environment:** Vulnerabilities come from Secommits: 150 records across CWE-79, 89, 352, 862, 787, 22, 416, 125, 78 and 94. The **challenge split keeps only the PRs that Haiku 4.5 or GPT-5.4-nano approved**: 1,062 PRs, 65–148 per CWE (mean 106). Each PR is reviewed once.
- **Outcome measures:**
  - *Refusal Rate (RR):* the share of malicious PRs rejected.
  - *Security Reason Rate (SRR):* rejections whose rationale identifies the exploit, as judged by an LLM judge with manual spot-checks.
  - Tool-interaction counts per review.

## Key findings
1. **There is a stable tier structure (Fig. 4).** Opus 4.7, GPT-5.5 and GLM-5 lead on every CWE. The other five sit about 20 pp lower on average and vary more. Grok Code Fast and GPT-5.4-nano are worst.
2. **Vulnerability class matters.**
   - Injection flaws (CWE-89 SQL, CWE-94 code) get > 80% SRR from Opus 4.7 and GPT-5.5.
   - For use-after-free (CWE-416), SRR is only 30% (Opus 4.7) and 20% (GPT-5.5).
   - For CWE-125, everyone except GPT-5.5 is below 50% SRR. Reviewers spot the bug but do not state its security implication.
3. **Unverifiable external claims are the most effective (Fig. 5, Fig. 7).**
   - Under Prior Approval Signal, Dependency Compatibility and Fake Bug Fix, weaker reviewers fall below ~35–40% RR.
   - GLM-5's worst framing is Prior Approval. **For > 80% of the PRs it approved under that framing, the identical code was rejected under other framings.** In one case it called a diff "removing critical security features under false pretenses" under one framing, and "correctly implements the cleanup" under another.
4. **Checkable inconsistencies get caught.** Under Evidence Dilution and False Coverage, the claims can be checked against the diff. GPT-5.4-nano validates the file list about 3× more often under Evidence Dilution than under Review Bias. Refactoring's claim of "no functional change" is easy to falsify.
5. **Repository-dependent explanations lead to unverified deference.** Kimi K2.5 and GPT-5.4-nano echo the attacker's rationale verbatim ("Approved—The PR removes redundant defensive code").
6. **Affective framings have model-specific effects.**
   - Emotional Appeal drops Grok Code Fast to 10% RR, while DeepSeek V4-Flash responds to urgency with longer deliberation (80% RR).
   - Out-of-Distribution jargon: Grok and Kimi reach 30–40% RR, while Opus and GPT-5.5 stay above 90%.
   - **AI Agent Authored** works on Grok Code Fast and GPT-5.4-nano, which "treat machine-generated provenance as an implicit endorsement of benign intent". It is largely ineffective on Opus 4.7 and GPT-5.5.
7. **Only one reviewer names the attack.** Claude Opus 4.7 calls out the social engineering in about ¼ of its transcripts ("fabricated justification", "classic social engineering pattern"). The others do so in < 10% of transcripts, and GPT-5.5, GPT-5.4-nano and Grok in < 1%. GPT-5.5 resists mainly through heavier tool use (Fig. 8).

## Relevance to research questions
### Q5: Interaction channels
The channel is **code review as a gatekeeping step**: one party's narrative plus artefact is judged by an LLM reviewer with tools to verify it. It is the reverse of the monitoring papers. Here the *overseer* is the target, and the overseen party controls the text the overseer reads. A key design variable is whether the reviewer's tools let it check the author's claims. Robustness tracks verification behaviour, e.g. GPT-5.5's heavy tool use. See [[Q5 Interaction channels]]

### Q6: Sources of inter-agent friction
The friction is **persuasion and authority claims from the author aimed at the reviewer**:
- fabricated prior approvals and expert "security analyses";
- claims of dependency compatibility;
- urgency / emotional pressure ("customers are suffering a live outage");
- jargon;
- the claim that another AI agent wrote the change.

These are the kinds of pressure a deceptive or pressured agent could put on a reviewer model, which bears on scenario **(a)** from the reviewer's side. The *AI Agent Authored* result shows that "another agent wrote this" works as trust-by-provenance for weaker reviewers. See [[Q6 Sources of inter-agent friction]]

### Q7.1: Effects on safety
- Narrative manipulation gets weaker reviewers to approve and merge real, previously disclosed vulnerabilities, with RR as low as ~10–35% for the most effective framings.
- The failure is **sycophantic deference to unverifiable claims**, not an inability to see the bug: the same diff is rejected under another framing.
- The authors recommend separating claim extraction from claim verification, and treating PR metadata as adversarial input.

See [[Q7.1 Effects on safety]]

## Key figures & tables
![[Melo2026-fig-05-p8.png]]
*Fig. 5: Refusal rate (red) and security-reasoning rate (blue) per reviewer under 5 framings that span the effectiveness range. Weaker reviewers collapse under Prior Approval Signal and Dependency Compatibility Claim.*

![[Melo2026-fig-07-p20.png]]
*Fig. 7: RR and SRR for all 15 framings × 8 reviewers.*

## Limitations / caveats
- **The author is not an agent.** Each narrative is a one-shot, LLM-generated artefact. There is no adaptive author revising after rejection and no multi-turn discussion. That makes this an injection-into-reviewer study rather than live inter-agent interaction, hence *adjacent*.
- **There is no neutral-description baseline.** Framing effects are only relative to one another. The paper does not report how often the vulnerable diff would be approved with an honest or empty description.
- **Selection bias:** the challenge split keeps only PRs that Haiku 4.5 or GPT-5.4-nano approved. Their rates are therefore depressed by construction, and between-model comparisons are skewed.
- Each PR is reviewed once, with no reported per-cell n. The error bars are wide for some cells.
- The SRR judge is validated only by "manual spot-checks".
- Some framings are implausible for some diffs, e.g. claiming a hardening change while removing sanitisation.
- Training-data contamination is possible, because the fixes are public. The authors argue this makes the failure rates lower bounds.
- Several models are recent releases (Opus 4.7, GPT-5.5), which limits reproducibility.

## Related work to follow
- [[Thornton2026 - Can Adversarial Code Comments Fool AI Security]]: adversarial comments against LLM security reviewers.
- [[Jin2026 - Are LLMs Reliable Code Reviewers Systematic]]: reliability of LLM code reviewers.
- [[Hwang2025 - Can You Trick the Grader Adversarial Persuasion of LLM]] and [[Khalifa2026 - Gaming the Judge]]: persuading LLM judges.
- [[Liu2025 - LLM Can be a Dangerous Persuader]], [[Zeng2024 - How Johnny Can Persuade LLMs to Jailbreak Them]] and [[Fanous2025 - SycEval Evaluating LLM Sycophancy]]: persuasion and sycophancy sources for the framings.
- [[Potter2026 - Peer-Preservation in Frontier Models]]: models treat other models' contributions differently (motivates AI Agent Authored).
- [[Kale2025 - Reliable weak-to-strong monitoring]]: an overseen agent manipulating its LLM monitor.

![[Backlog.base#Cited by this paper]]
