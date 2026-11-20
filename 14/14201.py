a = []
for x in range(1,2031):
    cnt = 0
    num = 3**100 -x
    while num:
        if num % 3 == 0:
            cnt += 1
        num= num//3
    a.append([cnt, x])
print(max(a))