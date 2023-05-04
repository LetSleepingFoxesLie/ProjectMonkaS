# This is the beginning of something... great? Possibly great?
# By the way, LSFM stands for "let sleeping foxes math."

import math

# Utility

def is_even(n: int) -> bool:
    """Returns whether a number is even or not.

    Args:
        n (int): The number you want to test.

    Returns:
        bool: Whether n is even or not.
    """
    return n % 2 == 0

def is_odd(n: int) -> bool:
    """Returns whether a number is odd or not.

    Args:
        n (int): The number you want to test.

    Returns:
        bool: Whether n is odd or not.
    """
    return n % 2 != 0

def is_prime(n: int) -> bool:
    """Checks whether a number is prime.

    Args:
        n (int): The number you want to test.

    Returns:
        bool: Whether n is prime.
    """
    
    div = 3
    upper_bound = math.ceil(math.sqrt(n))
    
    # Let's check some things beforehand
    
    # Exception handling in here maybe?
    
    # Case A: number is negative
    if n < 0:
        return False
    
    # Case B: number is either 0 or 1
    if n in range(0, 1):
        return False
    
    # Case C: number is 2
    if n == 2:
        return True
    
    # Case D: number is 3
    # lol, no
    
    # Main loop: checking for primality with a somewhat inefficient algorithm
    while div <= upper_bound:
        if n % div == 0:
            return False
        div += 2
    
    # If div has reached upper_bound, then it's a prime number!
    return True

def is_palindrome(arg: int | str) -> bool:
    """Checks whether arg is a palindrome.

    Args:
        arg (int | str): int or string to check whether it's a palindrome.

    Returns:
        bool: Whether arg is a palindrome.
    """
    
    if type(arg) is not str:
        arg = str(arg)
    
    # Reverses the string
    return arg == arg[::-1]

def count_divisors(n: int) -> int:
    """Returns the number of divisors of a number.

    Args:
        n (int): The number whose number of divisors you want to know.

    Returns:
        int: The number of divisors of n.
    """
    
    if n == 1:
        return 1
    
    # Let's make this much better, shall we?
    prime_factors = prime_factorization(n)
    divisors = 1
    
    for prime in prime_factors:
        divisors *= prime_factors[prime] + 1
        
    return divisors

# Generators
def generate_fibonacci_until_n(n: int) -> list:
    """Generates a list of Fibonacci numbers until n.

    Args:
        n (int): Generate up to this number (exclusive).

    Returns:
        list: A list of Fibonacci numbers until n.
    """
    
    # Initialize list
    fibonacci_list = list()
    
    # Initialize terms
    q, r = 0, 1
    
    # Fibonacci loop
    while r < n:
        dummy = q + r
        fibonacci_list.append(dummy)
        
        q = r
        r = dummy
    
    return fibonacci_list

def generate_divisors(n: int) -> list:
    """Generates the divisors of n.

    Args:
        n (int): The number whose divisors you want to find.

    Returns:
        list: A sorted list of divisors of n.
    """
    
    # Initializing variables
    divisors = [1]
    
    # Checking if n is 1
    if n == 1:
        return divisors
    
    div = 2
    upper_bound = math.ceil(math.sqrt(n))
    
    while div <= upper_bound:
        if n % div == 0:
            divisors.append(div)
            divisors.append(n // div)
        div += 1
    
    divisors.append(n)
    # Removing duplicated using set and list
    divisors = list(set(divisors))
    divisors.sort()
    #print(f"Div: {divisors} - Length {len(divisors)}")
    return divisors
    
def generate_prime_factors(n: int) -> list:
    """Decomposes a number into its prime factors.

    Args:
        n (int): The number you want to decompose.

    Returns:
        list: A list of the prime factors of n.
    """
    
    # We're going to take a relatively inefficient approach I guess.
    # I hope it's good enough!
    
    # Variables
    prime_factors = list()
    div = 3
    
    # My god, this code is looking so bad right now.
    # A white wolf would probably want to whack my face after this!
    if is_even(n):
        prime_factors.append(2)
        while is_even(n):
            n /= 2
    
    while n != 1:
        if n % div == 0:
            
            # Maybe write a utility function for this later
            if div not in prime_factors:
                prime_factors.append(div)
            
            n /= div
        else:
            # Generate next prime factor and set div to it
            # But we're taking the easy way out instead of doing that.
            # In this code, n should only be divisible by div if it's a prime factor.
            # Should, right? Right??
            
            div += 2
    
    return prime_factors

def prime_factorization(n: int) -> dict:
    """Generates the proper factorization of a number, exponents included.

    Args:
        n (int): The number you want to factor.

    Returns:
        dict: A dict with prime factors (as keys) and exponents (as values)
    """

    d = dict()
    
    if n == 1:
        return {1:1}

    prime = 2
    first_pass = True
    
    while n != 1:
        if n % prime == 0:
            if prime in d.keys():
                d[prime] += 1
            else:
                d[prime] = 1
            n //= prime
        else:
            if first_pass:
                prime += 1
                first_pass = False
            else:
                prime += 2
    
    return d

def generate_prime_list(n: int = 100) -> list:
    """Generates a list of the first n prime numbers.

    Args:
        n (int): The number of primes that should be in this list. Defaults to 100.

    Returns:
        list: A list of the first n prime numbers.
    """
    
    # Initializing variables
    prime_numbers = [2]
    number = 3
    count = 1
    
    # Main loop
    while count < n:
        if is_prime(number):
            prime_numbers.append(number)
            count += 1
        number += 2
        
    return prime_numbers

# Computation
def sum_of_natural_numbers(n: int) -> int:
    """Returns the sum of natural numbers from 1 to n.

    Args:
        n (int): Maximum number.

    Returns:
        int: The sum of all natural numbers from 1 to n.
    """
    return int((n * (n + 1) / 2))

def sum_of_squared_numbers(n: int) -> int:
    """Returns the sum of squared natural numbers from 1 to n.

    Args:
        n (int): Maximum number.

    Returns:
        int: The sum of all squared natural numbers from 1 to n.
    """
    return int((n * (n + 1) * (2 * n + 1)) / 6)

def nth_polygonal_number(index: int, sides: int) -> int:
    """Generates the index-th sides-gonal number.

    Args:
        index (int): The index of your polygonal number.
        sides (int): The number of sides of your polygon.

    Returns:
        int: The index-th sides-gonal number.
    """
    return int((sides - 2) * index * (index - 1) / 2) + index

def nth_triangular_number(n: int) -> int:
    """Generates the nth triangle number.

    Args:
        n (int): The index of the triangle number.

    Returns:
        int: The nth triangle number.
    """
    return nth_polygonal_number(n, 3)

def nth_square_number(n: int) -> int:
    """Generates the nth square number.
    Most useless function ever?

    Args:
        n (int): The index of the square number.

    Returns:
        int: The nth square number.
    """
    return n ** 2