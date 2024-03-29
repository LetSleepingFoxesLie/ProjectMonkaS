# Yes, I have done this before
# Yes, I might be more efficient this time

from math import sqrt, ceil

def sieve_of_eratosthenes(upper_bound: int) -> list:
    """Generates a list of prime numbers from 2 to upper_bound.
    Should be miles more efficient than my previous, naive-ish algorithm in lsfm.py.

    Args:
        upper_bound (int): The highest number to be checked against.
        This number must be 2 or higher!

    Returns:
        list: A list containing the prime numbers from 2 to n.
    """
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
    
    bool_list = [True] * (upper_bound + 1)
    index_offset = 2
    
    # This is where the sieve is running
    # There is something called the "segmented" sieve of Eratosthenes, but seems like too much work for me to implement
    loop_bound = ceil(sqrt(upper_bound))
    for i in range(index_offset, loop_bound):
        if bool_list[i]:
            j = i**2
            while j <= upper_bound:
                bool_list[j] = False
                j += i

    # And then generate the output list. I tried to create a list comprehension, but I hard struggled with it
    output_list = list()
    for i in range(index_offset, upper_bound + 1):
        if bool_list[i]:
            output_list.append(i)
            
    return output_list

def is_prime(n: int) -> bool:
    # I was planning on implementing the AKS primality test, but after looking at 
    # https://math.stackexchange.com/questions/2557694/aks-primality-test-vs-trial-division-performance
    
    # Then, I looked at the Miller-Rabin primality test... and it's apparently too cumbersome to implement.
    # It might see use down the line, but for now the good old trial division will be great, right?
    
    # Checks against negative integers, 0, 1, and even numbers all at once
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0:
        return False
    else:
        # The true primality test... by the OG trial division
        upper_bound = ceil(sqrt(n))
        for d in range(3, upper_bound, 2):
            if n % d == 0:
                return False
        return True

def factorize(n: int) -> list | dict:
    # Not quite sure yet.
    pass