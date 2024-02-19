import re

def pattern(str):
    p = r'ab*'
    if re.match(p, str):
        return True
    else:
        return False

str = str(input())
print(pattern(str))