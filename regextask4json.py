import json
import re

f = open("db.json")
parse = json.load(f)
pattern = r'\b[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}\b'
for i in parse:
    email = i.get("email")
    if(email and re.match(pattern, email)):
        print(email)
    