#filter,map,reduce (range 70–90, +10, product)

from functools import reduce

data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
print("Input List=",data)

filtered = list(filter(lambda x: x >= 70 and x <= 90, data))
print("List after filter =", filtered)

mapped = list(map(lambda x: x + 10, filtered))
print("List after map =", mapped)

result = reduce(lambda a, b: a * b, mapped)
print("Output of reduce =", result)
