a = []
for x in range(1,2031):
    cnt = 0
    num = 2**2025 + 2**2024 - 2**2021 - x
    while num:
        if num % 4 == 0:
            cnt += 1
        num= num//4
    a.append([cnt, x])
print(max(a))




