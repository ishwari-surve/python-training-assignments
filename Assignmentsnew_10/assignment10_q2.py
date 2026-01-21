#WAP which accepts one number and prints sum of first N natural numbers.

def sum_natural(no):
    total = 0
    for i in range(1,no+1):
        total = total + i
    print(total)

num = int(input("Enter a number:"))
sum_natural(num)
