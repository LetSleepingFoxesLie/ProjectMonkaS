# I don't even know how to approach this. I'm making commits as I figure this shit out.

from lsfm import prime_factorization
from utils.combinatorics import factorial

def test():
    q = prime_factorization(20)
    r = prime_factorization(52)

    print(q)
    print(r)
    
    are_exponents_in_both_dicts(q, r)
    print("======")
    s = merge_exponents_from_dicts(q, r)
    are_exponents_in_both_dicts(q, s)


def merge_exponents_from_dicts(q: dict, r: dict) -> dict:
    
    # Unpacking both dictionaries, and adding them
    output_dictionary = {**q, **r}
    
    # Now check for each key in output_dictionary if they exist in both q and r
    for k, v in output_dictionary.items():
        
        # And, if they do, we sum those pesky exponents
        if k in q and k in r:
            output_dictionary[k] = q[k] + r[k]
    print(output_dictionary)
    return output_dictionary

def are_exponents_in_both_dicts(number: dict, factorial: dict) -> bool:
    
    # We should check if all exponents in number are in factorial as well.
    n_keys = number.keys()
    f_keys = factorial.keys()
    
    # Debugging purposes:
    print(f"Number: {number}")
    print(f"Factorial: {factorial}")
    
    for key in n_keys:
        try:
            print(f"Checking for key: {key}")
            if number[key] > factorial[key]:
                print(f"Found key {key}, but of value higher than in number!")
                return False
        except KeyError:
            print(f"Key {key} not found! Returning false")
            return False
    
    print(f"All factors in factorial found! Returning true")
    return True

if __name__ == "__main__":
    test()