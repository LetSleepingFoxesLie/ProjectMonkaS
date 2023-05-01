# It's going to be the end of me. End moi.
from lsfm import is_even

# Maybe save shit into a dict with a chain length to sum?
chain_storage = {1:1}

global iterations
iterations = 0

# I'm so sorry, this code is a huge mess.
def main():
    for i in range(2, 1000000):
        global iterations
        iterations = 0
        
        # Stores the number of iterations in the current Collatz sequence as a key: value (number: iterations) pair.
        chain_storage[i] = collatz_sequence(i)
    
    # REturns the longest chain    
    longest_chain = max(chain_storage, key = chain_storage.get)
    print(f"Longest chain: number {longest_chain} -> {chain_storage[longest_chain]} chains.")

# The ugly, the ugly, and the ugly.
def collatz_sequence(number: int):
    global iterations
    
    # If number is found in keys, then return the sum of chains for that key with the current number of iterations
    if number in chain_storage.keys():
        return chain_storage[number] + iterations
    else:
        iterations += 1
        if number != 1:
            if is_even(number):
                return collatz_sequence(number // 2) # When dealing with recursion, we gotta return stuff!
            else:
                return collatz_sequence(3 * number + 1) # Absolutely didn't waste 30+ minutes trying to fix this out.
        else:
            return iterations

if __name__ == "__main__":
    main()