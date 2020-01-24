l = input().split()

out = []
if l[1] == '0':
    out.append('0 0')
else:
    for i in range(int(len(l) / 2)):
        a_i = int(l[2*i])
        n_i = int(l[2 * i + 1])
        if n_i != 0:
            out.append(str(a_i*n_i))
            out.append(str(n_i-1))

print(' '.join(out))

