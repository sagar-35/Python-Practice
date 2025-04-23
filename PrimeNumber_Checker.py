<<<<<<< HEAD
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter Any Number: "))

if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is NOT a Prime Number")
=======
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter Any Number: "))

if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is NOT a prime Number")
>>>>>>> 9849f6ebad0c1a9a80e6ca1bb3f9c64a9c979a97
