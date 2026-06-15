import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    first_line = file.readline()

candidate = json.loads(first_line)

print("\nCandidate ID")
print(candidate["candidate_id"])

print("\nCurrent Title")
print(candidate["profile"]["current_title"])

print("\nYears of Experience")
print(candidate["profile"]["years_of_experience"])

print("\nSkills")

for skill in candidate["skills"]:
    print(
        skill["name"],
        "|",
        skill["proficiency"]
    )