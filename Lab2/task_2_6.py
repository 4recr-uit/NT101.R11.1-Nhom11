from dependencies import install_dependencies
install_dependencies(["sympy"])
from random import randint
from sympy import randprime, prevprime, isprime

M10 = 2**89 - 1

def random_prime_generator():
    bits = [8, 16, 64]
    for k in bits:
        print(f"Random prime with {k} bits: {randprime(2**(k-1), 2**k)}\n")

def largest_primes_below(limit = M10, count = 10):
    print(f"{count} largest primes below {limit}:")
    p = limit
    for i in range(count):
        p = prevprime(p)
        print(f" - {i + 1}. {p}")

def check_prime():
    n = int(input("\nEnter a number smaller than 2^89 - 1: "))
    while n >= M10:
        print(f"Number must be smaller than {M10}.")
        n = int(input("Enter a number smaller than 2^89 - 1: "))
    if isprime(n):
        print(f"The number {n} is prime.")
        return
    print(f"The number {n} is not prime.")

def gcd(num1, num2):
    if num1 % num2 == 0: return num2
    return gcd(num2, num1 % num2)

def modular_exponentiation():
    a = int(input("Enter base (a): "))
    x = int(input("Enter exponent (x): "))
    p = int(input("Enter modulo (p): "))

    if x < 0:
        print("Exponent must be non-negative")
        return
    if p <= 0:
        print("Modulo must be positive")
        return

    original_a = a
    original_x = x
    result = 1
    a = a % p
    while x > 0:
        if x % 2 == 1:
            result = (result * a) % p

        a = (a * a) % p
        x = x // 2

    print(f"Result of {original_a}^{original_x} mod {p} is: {result}")

def main():
    print("===== TASK 2.6 =====")
    print("1. Random prime generator")
    random_prime_generator()
    print("2. Largest primes below 2^89 - 1")
    largest_primes_below()
    print("3. Check if a number is prime")
    check_prime()
    print("4. GCD of two numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")
    print("5. Modular exponentiation")
    modular_exponentiation()

if __name__ == "__main__":
    main()
