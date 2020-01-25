l = input().split()

def get_ret(a):
    if(a != 0):
        ret = str(a)
    else:
        ret = 'N'
    return ret

a = [0, 0, 0, 0, 0]
l2,l4 = 0, 0
for i in range(1, int(l[0])+1):
    n = int(l[i])
    if n%10 == 0:
        a[0] += n
    elif n%5 == 1:
        a[1] += ((-1)**l2)*n
        l2 += 1
    elif n%5 == 2:
        a[2] += 1
    elif n%5 == 3:
        a[3] += n
        l4 += 1
    elif n%5 == 4 and n > a[4]:
        a[4] = n

if l4 > 0:
    a[3] = '%.1f'%(a[3]/l4)
out = list(map(get_ret, a))
if l2 > 0 and out[1] == 'N':
    out[1] = str(0)
print(' '.join(out))