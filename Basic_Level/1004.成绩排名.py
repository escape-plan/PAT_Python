n = int(input())

l = []
min_score = 101
max_score = 0
min_idx = 0
max_idx = 0
for i in range(n):
    s = input()
    l.append(s.split())
    score = int(l[i][2])
    if score > max_score:
        max_score = score
        max_idx = i
    if score < min_score:
        min_score = score
        min_idx = i

print(l[max_idx][0] + " " + l[max_idx][1])
print(l[min_idx][0] + " " + l[min_idx][1])

# n = int(input())
#
# d = {}
# l = []
#
# for i in range(n):
#     a = input().split()
#     d[int(a[2])] = a[0] + ' ' + a[1]
#     l.append(int(a[2]))
#
# print(d[max(l)])
# print(d[min(l)])