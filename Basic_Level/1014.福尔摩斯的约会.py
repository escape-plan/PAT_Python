s1 = input()
s2 = input()
s3 = input()
s4 = input()
DAY = {'A':'MON', 'B':'TUE', 'C':'WED', 'D':'THU', 'E':'FRI', 'F':'SAT', 'G': 'SUN'}
HOUR = {'0': '00', '1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06',
        '7': '07', '8': '08', '9': '09', 'A': '10', 'B': '11', 'C': '12', 'D': '13',
        'E': '14', 'F': '15', 'G': '16', 'H': '17', 'I': '18', 'J': '19', 'K': '20',
        'L': '21', 'M': '22', 'N': '23'}

out = []
day = True
for i in range(min(len(s1),len(s2))):
    if s1[i] == s2[i]:
        if day and s1[i] in DAY.keys():
            out.append(DAY[s1[i]])
            day = False
        elif not day and s1[i] in HOUR.keys():
            time = HOUR[s1[i]] + ':'
            break

for i in range(min(len(s3),len(s4))):
    if s3[i] == s4[i] and s3[i].isalpha():
        if i < 10:
            time += '0'
        time += str(i)

out.append(time)
print(' '.join(out))