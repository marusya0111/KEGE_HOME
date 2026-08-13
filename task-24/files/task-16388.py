# ****KLMN
# KLMN***
# ***KLMN***
# KLMNKLMN***
# ***KLMNKLMN
# ***KLMN***KLMN

from re import finditer
with open ("task-24/data/24_16388.txt") as file:
    data = file.readline()

combo = r"KLMN"
pattern = rf"[KLMN]+{combo}+[KLMN]+{combo}?"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key=len)))

