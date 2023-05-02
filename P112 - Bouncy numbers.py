STARTING_NUMBER = 21780
STARTING_PERCENTAGE = 90.0
THRESHOLD = 99.0

# It''s critical to calculate the number of bouncy numbers previous to 21780!
STARTING_BOUNCY_NUMBERS = int(STARTING_PERCENTAGE * STARTING_NUMBER / 100)

from math import trunc

def main():
    
    # Don't forget to add 1 to the current number.
    # Lost a lot of time due to this oversight, damn.
    current_number = STARTING_NUMBER + 1
    bouncy_numbers = STARTING_BOUNCY_NUMBERS
    
    # Looks like a mess, doesn't it?
    # We basically check whether current_number is bouncy, then get the current percentage, and check against it.
    while True:
        if is_bouncy(current_number):
            bouncy_numbers += 1
        bouncy_numbers_percentage = calculate_percentage(bouncy_numbers, current_number)
        # print(f"Current percentage: {bouncy_numbers_percentage}%")
        if bouncy_numbers_percentage >= THRESHOLD:
            print(f"Threshold hit at number {current_number}!")
            break
        current_number += 1

# This is where the magic does (not) happen!
def is_bouncy(n: int) -> bool:
    return not (is_increasing(n) or is_decreasing(n))

# I wish this was better optimized!
# Update 2: giga optimized!!!!
def is_increasing(n: int) -> bool:
    stringified = [digit for digit in str(n)]
    
    # Only optimization I found before finishing this program:
    if "0" in stringified:
        return False
    
    # This snippet made the code so, so much faster!
    if stringified[-1] < stringified[0]:
        return False
    
    for index in range(len(stringified) - 1):
        if stringified[index + 1] < stringified[index]:
            return False
    return True

def is_decreasing(n: int) -> bool:
    stringified = [digit for digit in str(n)]
    
    # This snippet also made the code so, so much faster!
    if stringified[-1] > stringified[0]:
        return False
    
    for index in range(len(stringified) - 1):
        if stringified[index + 1] > stringified[index]:
            return False
    return True

# Utility stuff to calculate percentages and floats with a specific precision.
def calculate_percentage(bouncy_numbers: int, non_bouncy_numbers: int) -> float:
    percentage = bouncy_numbers / non_bouncy_numbers
    return decimal_precision(100 * percentage, 7)

def decimal_precision(number: float, digits: int) -> float:
    decimals = str(number).split('.')[1]
    
    if len(decimals) <= digits:
        return number
    
    truncator = 10.0 ** digits
    return trunc(number * truncator) / truncator

if __name__ == "__main__":
    main()