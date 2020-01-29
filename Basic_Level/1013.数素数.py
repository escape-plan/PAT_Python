M, N = tuple(map(int, input().split()))
Max = 104729    #第10000个素数
l = []
flag = [True]*(Max+2)
p = 2

while p <= Max:
    l.append(p)
    for i in range(2*p, Max, p):
        flag[i] = False
    while True:
        p += 1
        if flag[p]:
            break

out = 0
for i in range(M, N+1):
    out += 1
    if (out % 10 == 0):
        print(l[i-1])
    else:
        if i != N:
            print(l[i-1], end=' ')
        else:
            print(l[i-1], end='')