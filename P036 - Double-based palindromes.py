from utils.strings import is_palindrome
from utils.bases import dec_to_bin

# Small optimization cutting down runtime by half:
# As leading zeroes are NOT to be included, then
# we can add 2 to the previous number in each iteration.
# This is because no even number in binary ends with "1"

# Sum accumulator
s = 0

# Definitely runs under a minute, but I don't know how to optimize this!
for i in range(1, 10 ** 6 + 1, 2):
    b = dec_to_bin(i)
    d = i
    if is_palindrome(d) and is_palindrome(b):
        print(f"Palindrome found! s += {i} = {s + i}, {b}_2 = {d}_10")
        s += i

print(s)