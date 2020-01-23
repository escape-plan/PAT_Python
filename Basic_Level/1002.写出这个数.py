n = input()

sum = 0
for i in n:
    sum += eval(i)

l = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba','jiu']
print(' '.join(l[int(i)] for i in str(sum)))
