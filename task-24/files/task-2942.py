# Текстовый файл состоит из символов А, В и С.
# Определите максимальное количество идущих подряд пар символов АВ или АС в прилагаемом файле.
# Для выполнения этого задания следует написать программу

from re import finditer
test_1 = "ABAACCACABABACACAB"
t_1 = "AB*****AC****"


with open (r"24_2942.txt", encoding ="utf-8") as file:
    data = file.readline()

pattern = r"(AB|AC)+"
matches = [match.group() for match in finditer (pattern, data)]
print(len(max(matches, key = len )))








