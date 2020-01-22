cover_nums = []

def get_coverNums(n):
    nums = []
    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
        n /= 2
        nums.append(int(n))
    return nums

n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])
    cover_nums += get_coverNums(l[i])

cover_nums = list(set(cover_nums))
key_nums = [i for i in l if i not in cover_nums]
key_nums.sort(reverse=True)
i = 0
print(" ".join(str(i) for i in key_nums)) #一行代替下面循环
# while(i < len(key_nums)):
#     if (i == 0):
#         print(key_nums[i], end = '')
#     else:
#         print(' ' + str(key_nums[i]), end = '')
#     i+=1