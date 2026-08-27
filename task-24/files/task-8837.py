from re import finditer
with open ("task-24/data/24_8837.txt") as file:
    data = file.readline()

pattern = r"([A-W]+ +)+[A-W]+\."
matches = [match.group()  for match in finditer(pattern,data)]
print(len(max(matches, key=len)))
