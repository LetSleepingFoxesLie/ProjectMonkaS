# While this problem seems very hard at the surface level, a simple shift in perspective really shows how it's a simple problem.
# Like, really, really simple.

# But, for that, we're gonna need some combinatorics...

from utils.combinatorics import factorial

def main():
    print(calculate_lattice_paths(20))

def calculate_lattice_paths(grid_size: int) -> int:
    # Ok, so, what's happening in here?
    # At first glance, I expected recursion to play a role here and there, but that's not necessary.
    # Not at all.
    
    # I noticed that the number of movements to the right (R) must equal the number of downward steps (D).
    # If we represent a potential solution for the 2x2 case as a string of Rs and Ds, we get RRDD.
    # Or RDRD, or DDRR, or DRDR, or RDDR, or (finally) DRRD.
    # Oh, shit, they are... anagrams! Anagrams of 4 where 2 letters repeat themselves 2 times... for the 2x2 case.
    # So, it follows that:
    numerator = factorial(2 * grid_size)
    denominator = factorial(grid_size) * factorial(grid_size)
    return numerator // denominator

if __name__ == "__main__":
    main()