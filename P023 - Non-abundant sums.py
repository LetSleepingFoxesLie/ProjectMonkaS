from utils.numbers import get_divisors
from utils.primes import is_prime

THRESHOLD = 28123


def is_abundant(number: int) -> bool:
    divisors = get_divisors(number)[:-1]
    if sum(divisors) > number:
        return True
    return False

def get_abundant_numbers_list() -> list:
    abundant_numbers_list = list()
    for n in range(1, THRESHOLD):
        if n < 12 or not is_abundant(n):
            continue
        abundant_numbers_list.append(n)
    return abundant_numbers_list


def get_non_abundant_sum() -> int:
    
    abundant_numbers_list = get_abundant_numbers_list()
    
    s = 0
    for n in range(1, THRESHOLD):
        
        if n < 24:
            s += n
            continue
        
        found = False
        for m in abundant_numbers_list:
            if n - m < 12:
                continue
            if n - m in abundant_numbers_list:
                found = True
                print(f"Found for n = {n} -> {m} + {n - m}")
                break
            
        s += 0 if found else n
    
    return s

print(get_non_abundant_sum())
