#2.Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
