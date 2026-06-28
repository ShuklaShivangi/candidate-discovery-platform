import json
import csv

from scoring_v2 import CandidateScorer

# -----------------------------
# Load candidates
# -----------------------------

candidates = []

with open("data/candidates.jsonl", "r") as f:
    for line in f:
        candidates.append(json.loads(line))

scorer = CandidateScorer()

# -------------------------------------------------
# Stage 1 : Fast scoring (NO embeddings)
# -------------------------------------------------

print("Stage 1: Fast scoring...")

for candidate in candidates:

    candidate["light_score"] = (
        scorer.experience_score(candidate)
        + scorer.title_bonus(candidate)
        + scorer.education_bonus(candidate)
        + scorer.skill_score(candidate)
        + scorer.assessment_score(candidate)
        + scorer.recruiter_signal_score(candidate)
    )

# Sort by lightweight score

candidates.sort(
    key=lambda x: x["light_score"],
    reverse=True
)

# -------------------------------------------------
# Stage 2 : Embeddings only for Top 300
# -------------------------------------------------

TOP_K = 300

print(f"Stage 2: Running embeddings for Top {TOP_K} candidates...")

top_candidates = candidates[:TOP_K]

for i, candidate in enumerate(top_candidates, start=1):

    print(f"{i}/{TOP_K} : {candidate['candidate_id']}")

    candidate["final_score"] = (
        candidate["light_score"]
        + scorer.career_history_score(candidate)
    )

# -------------------------------------------------
# Final Ranking
# -------------------------------------------------

top_candidates.sort(
    key=lambda x: x["final_score"],
    reverse=True
)

top_score = top_candidates[0]["final_score"]

# -------------------------------------------------
# Generate CSV
# -------------------------------------------------

with open("submission.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(top_candidates[:100], start=1):

        score = round(candidate["final_score"] / top_score, 4)

        reasoning = (
            f'{candidate["profile"]["current_title"]} with '
            f'{candidate["profile"]["years_of_experience"]:.1f} yrs; '
            f'strong career match; '
            f'AI skills; '
            f'recruiter signals considered.'
        )

        writer.writerow([
            candidate["candidate_id"],
            rank,
            score,
            reasoning
        ])

print("submission.csv generated successfully!")