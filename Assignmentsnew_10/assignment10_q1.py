#WAP TO ACCEPT ONE NUMBER AND PRINTS MULTIPLICATION TABLE OF THAT NUMBER.

def print_table(no):
    for i in range(1,11):
        print(no*i,end=" ")

num = int(input("Enter a number:"))
print_table(num)
