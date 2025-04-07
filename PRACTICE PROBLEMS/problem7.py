# Write a program that prints all prime numbers between 1 and 100 using a for loop. Use the continue statement to skip non-prime numbers.

def isPrime(num):
    ranged = num // 2
    for i in range(2, ranged):
        if num % i == 0:
            return False
    return True

list_of_primes = [item for item in range(2, 100) if isPrime(item)]

print(list_of_primes)