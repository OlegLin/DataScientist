def slice_tup(tup, el):
  if el in tup:
    return tup[tup.index(el):]
  else:
    return tup
  
print(slice_tup((1, 2, 3, 4), 2))
print(slice_tup(('a', 'b', 'c', 'd'), 'd'))
print(slice_tup((1, 2, 3, 4), 5))
print(slice_tup(('a', 'b', 'c', 'd'), 'a'))
