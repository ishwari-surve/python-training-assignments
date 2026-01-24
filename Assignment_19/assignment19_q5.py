#filter prime, map ×2, reduce max

from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

data = [2, 70, 11, 10, 17, 23, 31, 77]
print("Input List",data)


filtered = list(filter(is_prime, data))
print("List after filter =", filtered)


mapped = list(map(lambda x: x * 2, filtered))
print("List after map =", mapped)


result = reduce(lambda a, b: a if a > b else b, mapped)
print("Output of reduce =", result)
