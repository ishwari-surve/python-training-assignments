#Q5. Accept one number and check whether it is divisible by 3 and 5
def CheckDivisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

# Function call
CheckDivisible(15)
