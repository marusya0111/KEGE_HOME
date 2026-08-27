# QR***S
# QS***R
# RS***Q
# RQ***S

from re import *
bukvi = r'[a-zA-Z]'
pattern = rf"({bukvi}*[QRS][^QRS]){bukvi}*"
matches = [match.group() for match in finditer (pattern, data)]










