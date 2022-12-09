a = input().split()
s = ''
for i in range(len(a)):
        s += a[i][0].upper() + a[i][1:] + ' '
print(s)
