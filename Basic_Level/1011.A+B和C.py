n = int(input())

for i in range(n):
    s = input().split()
    a, b, c = int(s[0]), int(s[1]), int(s[2])
    print("Case #{}: ".format(i+1) + str(a+b>c).lower())
