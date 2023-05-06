THRESHOLD = 10**6

# I don't care, let's brute force this.

def brute_force_constant() -> str:
    output = ""
    iterator = 0
    while len(output) <= THRESHOLD:
        iterator += 1
        output += str(iterator)
    
    print(output)
    return output

def answer(string: str):
    q = 1
    for i in range(7):
        if i == 0:
            digit = string[0]
        else:
            digit = string[10 ** i - 1]

        print(f"{10 ** i}-th digit of Champernowne is: {digit}")
        q *= int(digit)
    print(q)
    
answer(brute_force_constant())