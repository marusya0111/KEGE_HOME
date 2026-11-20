a= []
num = 2*2187**567 + 729**566 - 2*243**565 + 81**564 - 2*27**563 - 6561
cnt = 0
while num:
    num //= 27
    i = num % 27
    if i % 2 == 0 and  i > 9:
        cnt += 1
print(cnt)