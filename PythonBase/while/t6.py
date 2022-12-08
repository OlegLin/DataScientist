n = int(input())
k = ''
f = ''
for i in range(n):
        k = str(i+1) + k
        print(k)
for i in range(n, 0, -1):
        k = k[1:]
        print(k)

