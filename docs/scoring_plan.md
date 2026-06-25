# Candidate Discovery Platform - Scoring Plan (Version 2)


The ranking system should not rely on keyword matching alone.

Key principles:

* Skills = Claim
* Career History = Evidence
* Behavioral signals matter, but should not dominate technical fit.
* Technical fit is more important than recruiter/platform activity.
* Repeated mentions of the same topic should not earn repeated points.
* Only the most relevant recruiter signals are used.

---

# TECHNICAL SCORE

## 1. Experience Score

```text
0 <= years <= 9  -> round(years)
years > 9        -> 9
```

Examples:

```text
4.6 years -> 5
8.2 years -> 8
15 years  -> 9
```

Maximum Score: 9

---

## 2. Title Bonus

Relevant titles:

```text
AI Engineer
ML Engineer
Machine Learning Engineer
Data Engineer
Software Engineer
Backend Engineer
AI Specialist
NLP Engineer
Applied Scientist
MLOps Engineer
```

Score:

```text
Relevant Title -> +2
Otherwise      -> +0
```

Maximum Score: 2

---

## 3. Education Bonus

```text
Computer Science
Computer Engineering
Information Technology
Software Engineering
AI / ML related degree
```

Score:

```text
CS/IT Related Degree -> +1
Otherwise            -> +0
```

Maximum Score: 1

---

## 4. Skill Score

Only skills relevant to the JD are considered.

Proficiency scoring:

```text
beginner      -> +0.1
intermediate  -> +0.2
advanced      -> +0.3
```

Important:

* Only relevant skills score points.
* Irrelevant skills score 0.

Examples:

```text
NLP (advanced)       -> +0.3
Milvus (advanced)    -> +0.3
Photoshop            -> +0
Tailwind             -> +0
```

---

## 5. Assessment Score

Use Redrob skill_assessment_scores.

Formula:

```text
assessment_score / 100
```

Examples:

```text
95 -> 0.95
82 -> 0.82
61 -> 0.61
```

Rules:

* Only relevant assessment skills count.
* Irrelevant assessment skills score 0.

---

## 6. Career History Score

Career History is treated as the strongest technical signal.

Approach:

* Use embeddings.
* Compare Career History against technical requirements extracted from JD.
* Do not compare against the entire JD.
* Score unique relevant topics only.
* Repeated mentions of the same topic should not increase score.

Examples of relevant topics:

```text
retrieval
ranking
recommendation systems
vector databases
embeddings
LLMs
fine tuning
evaluation frameworks
search systems
production ML systems
```

Formula:

```text
Career History Score = Embedding Similarity × 30
```

Maximum Score: 30

---

# RECRUITER SIGNALS SCORE

Only 7 recruiter signals are used because they directly impact hiring probability.

---

## 7. Last Active Date

```text
0-30 days      -> +4
31-60 days     -> +3
61-90 days     -> +2
91-120 days    -> +1
120+ days      -> +0
```

---

## 8. Open To Work

```text
True   -> +5
False  -> +0
```

---

## 9. Notice Period

```text
0-30 days      -> +4
31-60 days     -> +2
61-90 days     -> +1
90+ days       -> +0
```

---

## 10. Recruiter Response Rate

```text
0-20%      -> +1
21-40%     -> +2
41-60%     -> +3
61-80%     -> +4
81-100%    -> +5
```

---

## 11. Profile Completeness

```text
0-25%      -> +1
26-50%     -> +2
51-75%     -> +3
76-100%    -> +4
```

---

## 12. Interview Completion Rate

```text
0-30%      -> +1
31-70%     -> +2
71-100%    -> +3
```

---

## 13. Willing To Relocate

```text
True   -> +2
False  -> +0
```

---

# IGNORED SIGNALS

The following signals are intentionally ignored:

```text
github_activity_score
offer_acceptance_rate
```

Reason:

* Not core hiring requirements for this role.
* Can unfairly penalize otherwise strong candidates.

---

# FINAL SCORE

```text
Final Score

=
Technical Score

+

Recruiter Signals Score
```

---

# Future Improvements (Version 3)

Possible future enhancements:

* Startup / Product Mindset Score
* Learning-to-Rank models
* Hybrid Retrieval (BM25 + Embeddings)
* LLM Re-ranking
* Dynamic weighting based on JD
* Explainable AI candidate matching dashboard
