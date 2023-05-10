# I'm going to brute force this crap apparently?

from utils.primes import is_prime, sieve_of_eratosthenes

def evaluate_quadratic(a: int, b: int, x: int) -> int:
    # As per the problem definition, f(x) = x^2 + an + b for |a| < 1000 and |b| <= 1000
    return (x ** 2) + a * x + b


# If f(x) must be prime, then, for x = 0, f(x) = b, which implies b must be prime as well!
# So we can reduce the search space by a lot. Instead of writing for b in range (-1000, 1001), we can use all primes from 1 to 1001

# Again, if f(x) must be prime, then, for x = 1, f(x) = 1 + a + b, which must be prime.
# If the RHS is prime, then it must be odd (barring when it's equal to 2), so 1 + a + b must also be odd.
# If b is a prime other than 2, then (1 + a) must be even, which is true if, and only if, a is also odd. Let's call this condition 1
# Likewise, if b is equal to two, then (1 + a) must be odd, in which case a must also be even. Let's call this condition 2

prime_list = sieve_of_eratosthenes(1001)
maximal_primes = 0
maximal_a: int
maximal_b: int

# Condition 1: a is even, because b is equal to 2
for a in range(0, 1002, 2):
    x = 0
    while(is_prime(evaluate_quadratic(a = a, b = 2, x = x))):
        x += 1

    if x > maximal_primes:
        maximal_primes = x
        maximal_a = a
        maximal_b = 2

# Condition 2: a is odd, because b is a prime (which is odd barring 2)
for a in range(-999, 1001, 2):
    for b in prime_list[1:]:
        x = 0
        while(is_prime(evaluate_quadratic(a = a, b = b, x = x))):
            x += 1

        if x > maximal_primes:
            maximal_primes = x
            maximal_a = a
            maximal_b = b
            print(f"Found maximal primes for a = {a} and b = {b}, totaling {x} primes!")

print(f"Maximum {maximal_a} x {maximal_b} = {maximal_a * maximal_b}, generating {maximal_primes} primes.")