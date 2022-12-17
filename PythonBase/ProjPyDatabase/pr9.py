spi = list(map(int, input().split()))
for i in range(len(spi)):
#  print(len(spi) - i - 1)
  spi.append(spi[len(spi) - i - 1])
#  print(spi)
  spi.pop(len(spi) - i - 2)

print(spi)
