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
    # Probably going to use AKS
    pass

def factorize(n: int) -> list | dict:
    # Not quite sure yet.
    pass