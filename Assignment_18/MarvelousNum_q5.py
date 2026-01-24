def ChkPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False

    return True
