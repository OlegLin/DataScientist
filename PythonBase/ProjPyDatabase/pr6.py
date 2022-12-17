a = [int(x) for x in input().split(',')]
b = [int(x) for x in input().split(',')]
c = set(a)
d = set(b)
print(abs(len(c)-len(d)))
