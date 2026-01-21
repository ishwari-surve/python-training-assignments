#print all even numbers till that number

def even_number(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i,end=" ")
num = int(input("Enter a number:"))
even_number(num)
