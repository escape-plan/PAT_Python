r = input().split()
n = int(r[0])
m = int(r[1])

l = list(input().split())
print(" ".join(l[n-m:]+l[:n-m]))
#print(" ".join(i for i in l[n-m:]+l[:n-m])) 这两种输出结果是一样的
