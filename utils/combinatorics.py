def factorial(n: int) -> int:
    """Returns the factorial of n.

    Args:
        n (int): Number.

    Returns:
        int: The factorial of n (n!).
    """
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)
    
def anagrams(word: str) -> int:
    # To be added
    pass

def permutations():
    pass

def binomial_coefficient(n: int, k: int) -> int:
    """Returns the binomial coefficient of C(n, k).
    Also known as "n choose k." in combinatorics.

    Args:
        n (int): n
        k (int): k

    Returns:
        int: C(n, k)
    """
    # We cannot apply this function to negative numbers... or when k > n
    if k < 0 or k > n:
        return 0
    
    # C(n, 0) = 1, and C(n, n) = 1
    if k == 0 or k == n:
        return 1
    
    # Because C(n, k) = C(n, n - k)
    k = min(k, n - k)
    
    # Calculating the coefficient for once using an iterative approach to avoid factorials
    # They can get really, really inefficient when dealing with higher numbers due to high recursion levels
    coefficient = 1
    for iterator in range(k):
        coefficient = coefficient * (n - iterator) // (iterator + 1)
    
    return coefficient

def permutations(n: int, k: int) -> int:
    """Returns the number of permutations given (n, k).
    This function is used when the order of the arrangement matters.
    P(n, k) = n!/(n-k)!

    Args:
        n (int): n
        k (int): k

    Returns:
        int: P(n, k)
    """
    
    # Once more, we're checking for some stuff
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    numerator, denominator = 1, 1
    for i in range(n):
        numerator *= i + 1
    for i in range(n - k):
        denominator *= i + 1
        
    return numerator // denominator

def combinations(n: int, k: int) -> int:
    """Returns the number of combinations given (n, k).
    C(n, k) = n!(k!(n-k)!)
    Args:
        n (int): n
        k (int): k

    Returns:
        int: C(n, k)
    """
    return binomial_coefficient(n, k)