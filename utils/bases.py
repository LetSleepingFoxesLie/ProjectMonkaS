# Let's create a base converter! Or multiple of those... from scratch!

def dec_to_base(dec: int, base: int) -> str:
    """Converts a decimal number to another base.

    Args:
        dec (int): The decimal number you want to convert.
        base (int): The base to which you want to convert.

    Returns:
        str: A string with in the dec_base format.
    """
    if not (2 <= base <= 36):
        print("dec_to_base only accepts bases in [2, 36]!")
        return ""
    
    if dec < 1:
        print("dec_to_base only accepts positive decimal numbers!")
        return ""
    
    # Converted base generator
    converted: str = str()
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
    
    while dec >= base:
        converted += ALPHABET[dec % base]
        dec //= base
    converted += ALPHABET[dec]
    
    # Reverses the string
    return converted[::-1]

def base_to_dec(encoded: int | str, base: int) -> int:
    """Converts a number in another base to decimal.

    Args:
        encoded (int | str): The encoded number.
        base (int): The base in which it is encoded.

    Returns:
        int: The number in base 10 (decimal)
    """
    if not (2 <= base <= 36):
        print("base_to_dec only accepts bases in [2, 36]!")
        return ""

    
    if type(encoded) == int:
        if encoded < 1:
            print("base_to_dec only accepts natural numbers higher than 1!")
            return ""
        encoded = str(encoded)
    encoded = encoded[::-1]
    
    converted, iterations = 0, 0
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
    for char in str(encoded):
        index_in_alphabet = ALPHABET.find(char)
        if index_in_alphabet > base:
            print(f"Invalid encoded string found! Aborting loop.")
            return ""
        converted += index_in_alphabet * (base ** iterations)
        iterations += 1
    
    return converted
        
        

# Some useful ones

def dec_to_bin(dec: int) -> str:
    return dec_to_base(dec, 2)

def dec_to_oct(dec: int) -> str:
    return dec_to_base(dec, 8)

def dec_to_hex(dec: int) -> str:
    return dec_to_base(dec, 16)

def dec_to_b32(dec: int) -> str:
    return dec_to_base(dec, 32)

def dec_to_b36(dec: int) -> str:
    return dec_to_base(dec, 36)

# Another useful ones

def bin_to_dec(enc: int | str) -> int:
    return base_to_dec(enc, 2)

def oct_to_dec(enc: int | str) -> int:
    return base_to_dec(enc, 8)

def hex_to_dec(enc: int | str) -> int:
    return base_to_dec(enc, 16)

def b32_to_dec(enc: int | str) -> int:
    return base_to_dec(enc, 32)

def b36_to_dec(enc: int | str) -> int:
    return base_to_dec(enc, 36)

# And the most uselesstest of them all!
#def dec_to_dec(dec: int) -> str:
#    return dec_to_base(dec, 10)

# print(dec_to_oct(257))
# print(oct_to_dec(dec_to_oct(257)))