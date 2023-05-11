# We're not going to generate any permutations for this. I hope it works!

from utils.combinatorics import factorial

factorials = [factorial(i) for i in range(0, 10)][::-1]

# We're going to use proportions to generate the string... as each number must appear once!
# 10! = 3,628,800, so there are 9! = 362,880 possible permutations for each starting digit.
# Thus, there are 8! = 40320 possible permutations for each set of 2 starting digits...
# If they are sorted in "lexicographic" order, then we can use proportions to draw out conclusions about the numbers we're looking for.

# In short, we're looking for the coefficients a, b, c, d, e, f, g, h, i, j so that:
# 10^6 = 9! * (a/9) + 8! * (b/8) + 7! * (c/7) + ... + j
# Then, abcdefghij will be the string we're looking for.

def get_nth_lexicographic_permutation(nth: int) -> int:
    
    # Slicing the list
    digits = [i for i in range(0, 10)]
    s = str()
    
    # For each digit...
    for digit in range(0, 10):
        
        # Gets the coefficient for the (coefficient / n!) part
        index = nth // factorials[digit]
        
        # nth CANNOT be zero at any point unless it's at the end.
        if nth % factorials[digit] == 0:
            index -= 1
        
        # And this gets the remainder
        nth -= index * factorials[digit]
        
        # Retrieves the digit, which must be unique, and updates the string
        s += str(digits[index])
        
        # print(f"Found {index} x {factorials[digit]} ({9 - digit}!). New nth = {nth} -> {s}.")
        
        # Pops index
        if len(digits) != 0:
            digits.pop(index)
            
        # print(f"Digit {digit}, digits {digits}")
            
    return s
    
print(get_nth_lexicographic_permutation(10**6))