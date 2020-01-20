cnt = 0
n = eval(input())

while n != 1:
    if n%2 != 0:
        n = 3*n + 1
    n /= 2
    cnt += 1

print(cnt)
