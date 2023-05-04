# I don't even know how to approach this. I'm making commits as I figure this shit out.

from lsfm import prime_factorization, is_prime
from utils.combinatorics import factorial

def main():
    # Let's try for the case of S(100) = 2012... shall we?
    THRESHOLD = 10**2
    
    # We're starting the sum at 1 because 1% % 1 == 0... we should start at 2, but I don't care. Let the algorithm cook!
    # Actually, nevermind, the thing asks us to check from 2 <= i <= n
    SUM = 0
    
    for n in range(2, THRESHOLD + 1):
        
        # Otherwise... factor n into its prime factors and iterate, from 1 to n, until m % n == 0... but we'll be cleverer... I guess?
        # Commit 4: actually, we'll have to do this regardless of whether n is prime or not... see below \/
        n_factors = prime_factorization(n)
        
        # First optimization measure: if n is prime, then the smallest number m such that n divides m! is n... so m must be equal to n
        if is_prime(n):
            SUM += n
            print(f"{n} is prime!")
            continue
        
        # And here comes the loop in which we'll check for m
        m_factors = dict()
        
        SUM += get_smallest_number_m_such_that_n_divides_m_factorial(n, n_factors, m_factors)
        
        if n % 10000 == 0:
            print(f"Going strong at n = {n}")
    
    print(f"S({THRESHOLD}) = {SUM}")

def test():
    
    q = prime_factorization(20)
    r = prime_factorization(52)

    print(q)
    print(r)
    
    are_exponents_in_both_dicts(q, r)
    print("======")
    s = merge_exponents_from_dicts(q, r)
    are_exponents_in_both_dicts(q, s)

def gnf_test():
    
    test_d = dict()
    for i in range(1, 150):
        print(f"Adding the factors of {i}! to test_d")
        test_d = get_next_factorial(i, test_d)


def merge_exponents_from_dicts(q: dict, r: dict) -> dict:
    
    # Unpacking both dictionaries, and adding them
    output_dictionary = {**q, **r}
    
    # Now check for each key in output_dictionary if they exist in both q and r
    for k, v in output_dictionary.items():
        
        # And, if they do, we sum those pesky exponents
        if k in q and k in r:
            output_dictionary[k] = q[k] + r[k]
    # print(output_dictionary)
    return output_dictionary

def get_next_factorial(n: int, current_dict: dict) -> dict:
    next_factorial = get_next_factorial(n, current_dict)
    return merge_exponents_from_dicts(current_dict, next_factorial)

# This is fugly
def get_smallest_number_m_such_that_n_divides_m_factorial(upper_bound: int, n_factors: dict, m_factors: dict) -> int:
    m = 2

    while m <= upper_bound:
        m_factors = get_next_factorial(m, m_factors)
        if are_exponents_in_both_dicts(n_factors, m_factors):
            print(f"Found an m = {m}")
            return m
        m = return_next_key_if_prime(m, n_factors)
    return m

def are_exponents_in_both_dicts(number: dict, factorial: dict) -> bool:
    
    # We should check if all exponents in number are in factorial as well.
    n_keys = number.keys()
    f_keys = factorial.keys()
    
    # Debugging purposes:
    # print(f"Number: {number}")
    # print(f"Factorial: {factorial}")
    
    for key in n_keys:
        try:
            # print(f"Checking for key: {key}")
            if number[key] > factorial[key]:
                # print(f"Found key {key}, but of value higher than in number!")
                return False
        except KeyError:
            # print(f"Key {key} not found! Returning false")
            return False
    
    # print(f"All factors in factorial found! Returning true")
    return True

def return_next_key_if_prime(current_number: int, n_factors: dict) -> int:
    
    if current_number == 2 or current_number == 3:
        return current_number + 1
    
    for k in n_factors.keys():
        if current_number >= k:
            continue
        else:
            return k if is_prime(k) else current_number + 1

if __name__ == "__main__":
    # gnf_test()
    main()