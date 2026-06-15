import json

important_skills = [
    "NLP",
    "Fine-tuning LLMs",
    "Milvus",
    "LoRA"
]

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for i, line in enumerate(file):

       if i == 9:
        candidate = json.loads(line)
        print(candidate)
        break

        candidate = json.loads(line)

        score = 0

        if candidate["profile"]["years_of_experience"] >= 5:
            score += 10

        if candidate["profile"]["current_title"] == "Backend Engineer":
            score += 10

        for skill in candidate["skills"]:
            if skill["name"] in important_skills:
                score += 5

        print(
            candidate["candidate_id"],
            "|",
            candidate["profile"]["current_title"],
            "| Score:",
            score
        )