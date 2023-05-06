from lsfm import is_prime, generate_prime_list

THRESHOLD = 5000
lookup_dict = dict()
big_prime_list = generate_prime_list(500)

# Let's get a feeling for this problem!

# First, let's pregenerate the first few primes
# Second, let's iterate for each number
# I don't know
# We'll have to recursively iterate stuff from what I'm gathering and use some caching/memoization
# I believe the main catch we should be looking to implement is to recursively iterate from n to 1 instead of 1 to n... right?

def get_prime_summations(n: int) -> int:
    # Let's work iteratively from n to 1:
    global lookup_dict
    
    # If n is already cached, return it
    if n in lookup_dict.keys():
        return lookup_dict[n]
    else:
        # We're going to calculate it and write it somewhere...
        
        ways = 0
        # Using a loop to go from n to 1/2:
        for prime in big_prime_list:
            if prime > n:
                break
            if prime == n:
                ways += 1
                break
            ways += get_prime_summations(n - prime)
        
        # Write the result to cache
        lookup_dict[n] = ways
        print(ways)
        
        # And return ways
        return ways

print(get_prime_summations(10))
print(lookup_dict)