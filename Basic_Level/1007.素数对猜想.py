n = int(input())

def is_prime(n):        #加强版判断素数方法
    if n == 2 or n == 3:
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    tps = int(n ** 0.5)
    for i in range(5, tps + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

cnt = 0
flag = True     #是否第一个素数
last = 0        #上一个素数
for i in range(2, n+1):
    if(is_prime(i)):
        if(flag):
            last = i
            flag = False
        else:
            if (i - last == 2):
                cnt += 1
            last = i
print(cnt)

# 最后一个测试点超时不能通过，C++这个办法应该能通过，谁让我要用Python呢
# n = int(input())
# def is_prime(n):          #一般判断素数办法
#     for i in range(2, int(n**0.5)+1):
#         if(n%i == 0):
#             return False
#     return True
# def get_primeList(n):
#     l = []
#     for i in range(2, n+1):
#         if(is_prime(i)):
#             l.append(i)
#     return l
#
# l = get_primeList(n)  #对这个地方，上面也有优化，没必要保存这个数组进行二次遍历
# cnt = 0
# for i in range(len(l)-1):
#     if l[i+1] - l[i] == 2:
#         cnt += 1
#
#print(cnt)
