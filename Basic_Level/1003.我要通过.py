'''
1.字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
2.任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
3.如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
aPATc aPAATca
'''
n = eval(input())

for i in range(n):
    s = input()

    n_p = s.count('P')
    n_t = s.count('T')
    n_a = s.count('A')
    p_idx = s.find('P')
    t_idx = s.find('T')
    s1 = s[:p_idx]
    s2 = s[t_idx+1:]
    s3 = s[p_idx+1:t_idx]
    if sum([n_p, n_a, n_t]) != len(s):
        print('NO')
    elif n_p != 1 or n_t != 1:
        print('NO')
    elif t_idx < p_idx or s2 != s1*s3.count('A') or len(s3) == 0:
        print('NO')
    else:
        if(s1.count('A') != len(s1) or s2.count('A') != len(s2) or s3.count('A') != len(s3)):
            print('NO')
        else:
            print('YES')
