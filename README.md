# Candidate Discovery Platform

## Intelligent Candidate Discovery using AI

An AI-powered candidate ranking system developed for the **Redrob × Hack2Skill India Runs Challenge**.

## Overview

Traditional recruitment systems rely heavily on keyword matching, often overlooking highly relevant candidates. This project introduces an intelligent candidate ranking engine that combines structured profile analysis, recruiter behavioral signals, and semantic similarity to identify the best-fit candidates.

The system generates an explainable ranked shortlist while remaining computationally efficient through a two-stage ranking strategy.

---

## Features

- Intelligent Job Description understanding
- Multi-factor candidate scoring
- Recruiter behavioral signal integration
- Semantic career-history matching using Sentence Transformers
- Explainable candidate ranking
- Hybrid ranking pipeline for faster execution
- Automatic Top-100 candidate shortlist generation

---

## Project Structure

```
candidate-discovery-platform/
│
├── data/
│   ├── candidates.jsonl
│   ├── sample_candidates.json
│   ├── job_description.docx
│
├── src/
│   ├── scoring_v2.py
│   ├── generate_submission.py
│
├── docs/
│
├── requirements.txt
├── README.md
└── submission.csv
```

---

## Technologies Used

- Python
- Sentence Transformers (all-MiniLM-L6-v2)
- Scikit-learn
- python-docx
- OpenPyXL
- NumPy
- Pandas

---

## Ranking Methodology

Each candidate is evaluated using multiple signals:

- Experience
- Job Title Relevance
- Education
- Technical Skills
- Skill Assessment Scores
- Recruiter Signals
- Career History Semantic Similarity

To improve runtime, lightweight scoring is first applied to all candidates. Semantic similarity is then computed only for the top-ranked candidates before generating the final ranked shortlist.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python src/generate_submission.py
```

---

## Output

The system generates:

```
submission.csv
```

containing:

- candidate_id
- rank
- score
- reasoning

---

## Author

**Shivangi Shukla**

