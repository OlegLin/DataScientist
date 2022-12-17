a = 1
b = 10
d = 1

c = a + 1
if a * c >= a * b:
        print(2)
else:
        count = 1
        while d * c < a * b:
                d *= c
                c += 1
                count += 1
        print(count)
