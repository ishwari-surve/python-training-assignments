#Reverse a Number

def reverse_number(num):
    reverse = 0

    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return reverse


number = int(input("Enter a number: "))
print(reverse_number(number))
