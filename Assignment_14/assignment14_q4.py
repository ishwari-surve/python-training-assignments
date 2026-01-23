#Minimum of two numbers

minimum = lambda a, b: a if a < b else b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(minimum(x, y))
