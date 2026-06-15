import json
from pprint import pprint

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    first_line = file.readline()

candidate = json.loads(first_line)

pprint(candidate)