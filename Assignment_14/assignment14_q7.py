#Check divisible by 5

div_by_5 = lambda x: True if x % 5 == 0 else False

num = int(input("Enter a number: "))
print(div_by_5(num))
