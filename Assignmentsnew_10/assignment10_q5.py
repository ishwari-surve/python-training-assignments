#print all odd numbers till that number

def odd_numbers(n):
    for i in range(1,n+1):
        if i % 2 != 0:
            print(i,end=" ")
num = int(input("Enter a number:"))
odd_numbers(num)
