import json
import re

f = open('db.json')
parse = json.load(f)
total_gpa = 0
cnt = 0
for i in parse:
    total_gpa += i["gpa"]
    cnt += 1
avgGpa = total_gpa / cnt
print(avgGpa)