# Very naive implementation... it gives the correct result for n = 1000 (15864), but it's a very naive algorithm as it checks for every value between 2 and upper_bound - 2

def convert_to_base(number: int, base: int) -> list:
    converted = list()
    
    if base > number:
        return -1
    
    while number >= base:
        k = number % base
        if k != 1:
            return converted[::-1]
        converted.append(number % base)
        number //= base
    converted.append(number)
    return converted[::-1]


def has_only_ones(converted_base: list) -> bool:
    converted_base = [str(n) for n in converted_base]
    return len(converted_base) == converted_base.count('1')

def is_strong_repunit_naive(number: int) -> bool:
    # I know for a fact that all numbers are at least a repunit of its b_(predecessor) form
    # We must find a way to better optimize the upper bound...
    
    # Maybe the upper bound must be number / base?
    upper_bound = int((number ** 0.666))
    for base in range(2, upper_bound - 2):
        converted = convert_to_base(number, base)
        if has_only_ones(converted):
            print(f"Number {number} has a repunit in base {base}! ({number}_{base} = {convert_to_base(number, base)})")
            return number
        else:
            continue
    return 0

s = 1
for i in range(1, 100000):
    if is_strong_repunit_naive(i):
        s += i

print(s)