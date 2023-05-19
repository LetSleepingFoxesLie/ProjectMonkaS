fifth_powers = [i ** 5 for i in range(0, 10)]

def is_digit_fifth_power(number_as_string: str | int) -> bool:
    if type(number_as_string) == str:
        number_as_string = int(number_as_string)
        
    digits = [int(digit) for digit in str(number_as_string)]
    
    s = 0
    for d in digits:
        s += fifth_powers[d]
    
    # print(f"s = {s}, digits = {digits}")
        
    return s == number_as_string

# Guesswork: the largest digit is 9, so the upper bound must be around u(n) = 9^5 * n.
# For n = 4, 5, u(n) > 10^n
# The first value for which the inequality inverts is n = 6... so I assume the upper bound must be u(6)
def main():
    THRESHOLD = 6 * (9 ** 5)
    s = 0
    for i in range(2, THRESHOLD):
        s += i if is_digit_fifth_power(i) else 0
    print(s)

if __name__ == "__main__":
    main()
    
    