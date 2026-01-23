#Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)
