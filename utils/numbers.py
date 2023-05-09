import math

def get_divisors(n: int) -> list:
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