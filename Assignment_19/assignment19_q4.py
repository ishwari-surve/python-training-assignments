#filter even, map square, reduce addition

from functools import reduce

data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
print("Input List=",data)


filtered = list(filter(lambda x: x % 2 == 0, data))
print("List after filter =", filtered)


mapped = list(map(lambda x: x * x, filtered))
print("List after map =", mapped)


result = reduce(lambda a, b: a + b, mapped)
print("Output of reduce =", result)
