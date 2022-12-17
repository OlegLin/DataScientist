n = int(input())

tug = n // (17 * 13)
cho = (n - (tug * (17 * 13))) // 13
ost = (n - (tug * (17 * 13))) % 13
print(tug, cho, ost)
