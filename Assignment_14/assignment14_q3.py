#Maximum of two numbers

maximum = lambda a, b: a if a > b else b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(maximum(x, y))
