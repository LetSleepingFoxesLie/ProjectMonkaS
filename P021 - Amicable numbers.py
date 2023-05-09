from utils.numbers import get_divisors

# 10^8... there's a way to make this faster, isn't there?
s = 0
"""
for i in range(1, 10000):
    for j in range(1, 10000):
        if i == j:
            continue
        if sum(get_divisors(i)) == sum(get_divisors(j)):
            s += i + j
"""

# Ain't it a bit hacky?
for i in range(10, 10000):
    
    # Instead of running two loops, we're checking everything in one loop
    j = sum(get_divisors(i)) - i
    if i < j or i == j:
        continue
    if i == sum(get_divisors(j)) - j:
        print(f"Found an amicable pair! Numbers {i} and {j}")
        s += i + j

print(s)