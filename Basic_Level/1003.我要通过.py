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
    elif n_p != 1 or n_t != 1 or t_idx < p_idx:
        print('NO')
    elif s2 != s1*s3.count('A') or len(s3) == 0:
        print('NO')
    elif s1.count('A') != len(s1) or s2.count('A') != len(s2) or s3.count('A') != len(s3):
        print('NO')
    else:
        print('YES')
