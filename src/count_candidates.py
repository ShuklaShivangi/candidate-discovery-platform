import json
import time

start = time.time()

count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        json.loads(line)
        count += 1

end = time.time()

print("Total candidates:", count)
print("Time taken:", round(end - start, 2), "seconds")