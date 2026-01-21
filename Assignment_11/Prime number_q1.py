#checks prime number or not

def is_prime (no):
    if no <= 1:
        return False
    
    for i in range(2,no):
        if no % 1 == 0:
            return False
    return True

number = int(input("Enter a number:"))

if is_prime(number):
    print("Prime number")
else:
    print("Not a Prime number")
