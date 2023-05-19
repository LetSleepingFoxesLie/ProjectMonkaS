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
    
    # Let's try to "sieve" through this thing first, shall we?
    
    # The idea:
    # 1. Generate a [True] array of THRESHOLD size
    # 2. Create two iterators: i and j, which represent their current indexes in abundant_numbers_list
    # 3. Let v[i] and v[j] be their values. Return the value at their indexes and set array[v[i] + v[j]] to False
    # This looks a bit like the Sieve of Eratosthenes... doesn't it?
    k = [True] * THRESHOLD
    for i in range(len(abundant_numbers_list)):
        for j in range(i, len(abundant_numbers_list)):
            index = abundant_numbers_list[i] + abundant_numbers_list[j]
            if index >= THRESHOLD:
                continue
            k[index] = False
            
    # 4. Finally, return the sum of all indexes where k[i] is set to True
    s = 0
    for i in range(len(k)):
        s += i if k[i] else 0
    
    # I haven't timed it, but it spits the answer in around 2.5-3 seconds?
    return s


def get_non_abundant_sum_unoptimized() -> int:
    
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
