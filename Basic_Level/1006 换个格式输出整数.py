s = input()
out = ''
l = ['B', 'S']
for idx, i in enumerate(s):
    loc = len(s)-idx
    if(loc == 3):
        out += l[0] * int(i)
    elif(loc == 2):
        out += l[1] * int(i)
    elif(loc == 1):
        for j in range(1,int(i)+1):
            out += str(j)
print(out)