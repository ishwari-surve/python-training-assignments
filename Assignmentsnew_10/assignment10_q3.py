#Factorial of number

def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact=fact*i
    print(fact)

num = int(input("Enter a number:"))
factorial(num)
