import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    first_line = file.readline()

candidate = json.loads(first_line)

score = 0

if candidate["profile"]["years_of_experience"] >= 5:
    score += 10

if candidate["profile"]["current_title"] == "Backend Engineer":
    score += 10

print("Candidate:", candidate["candidate_id"])
important_skills = [
    "NLP",
    "Fine-tuning LLMs",
    "Milvus",
    "LoRA"
]

for skill in candidate["skills"]:
    if skill["name"] in important_skills:
        score += 5
print("Score:", score)