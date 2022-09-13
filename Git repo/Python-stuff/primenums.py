def prime_check(num):
    if num == 1:
        return True
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            return False
        else:
            return True
print(prime_check(165))