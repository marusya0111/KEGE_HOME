# 8*9 - 6
# 01-5*100
# 8+*10
# -9-10
# +99
#

from re import finditer
with open ("task-24/data/24_17685.txt") as file:
    data = file.readline()

number = r"[1-9][0-9]*"
pattern = rf"({number}[+*])+{number}"
matches = [match.group() for match in finditer(pattern,data)]

