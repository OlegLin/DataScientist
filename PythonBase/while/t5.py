les = int(input())



for i in range(les):
        k = str(1) * (i+1)
        print(' '*(les - i - 1), int(k) ** 2, sep='')

        
for j in range(les - 1, 0, -1):
        k = str(1) * (j)
        print(' '*(les - j ), int(k) ** 2, sep='')
