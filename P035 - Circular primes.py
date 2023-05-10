from utils.primes import sieve_of_eratosthenes


# We'll do this by appending number to itself as a string, and then slicing it
def generate_rotations_of_number(number: int) -> list:
    l = list()
    k = str(number) + str(number)
    for digit in range(len(str(number))):
        
        # String slicing without having to resort to modulo operation
        s = k[digit:digit + len(str(number))]
        if s in l:
            continue
        l.append(int(s))
    return l

# Generates a prime list through the sieve of Eratosthenes, and then check if it exists within the list
prime_list = sieve_of_eratosthenes(1000001)

def are_all_rotations_prime(rotations: list) -> bool:
    for rotation in rotations:
        if rotation not in prime_list:
            return False
    return True

def has_bad_digit(n: int) -> bool:
    bad_digits = ["0", "2", "4", "5", "6", "8"]
    for d in bad_digits:
        if d in str(n):
            return True
    return False

# Where the magic happens
circular_primes = 0
THRESHOLD = 10 ** 6

# Little optimizations: 
# 1. If there is an even number in the number itself, one of the rotations will be even, which is not prime
# 2. Same goes if there's a 5, as one of the rotations will be divisible by 5
for p in prime_list:
    
    if has_bad_digit(p) and p > 9:
        continue
    
    rotations = generate_rotations_of_number(p)
    if are_all_rotations_prime(rotations):
        circular_primes += 1

print(f"There are {circular_primes} circular primes below {THRESHOLD}!")