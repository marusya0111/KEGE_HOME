from re import *
from string import ascii_uppercase

pattern = rf"[02468]{bukvi}*[02468]"


pattern = r'[02468][A-Z]+[02468]'

matches = [match.group() for match in finditer (pattern, data)]
ans = 0
for match in matches:
    if len(set(match[1:-1])) == 1:
        ans - max(ans,len(match))
print(ans)

################################################
for letter in ascii_uppercase:
    pattern = rf'[02468]{letter}+[02468]'
    matches = [match.group() for match in finditer(pattern, data)]
    ans = max(ans,len(max(matches, key = len )))