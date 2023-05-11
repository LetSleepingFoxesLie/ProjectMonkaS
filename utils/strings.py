# I'm not sure how useful these things are after all, huh

def is_palindrome(a: str | int) -> bool:
    """Checks whether a number or a string is a palindrome.

    Args:
        a (str | int): input

    Returns:
        bool: Whether "a" is a palindrome.
    """
    if type(a) == int:
        a = str(a)
    
    return a == reverse_string(a)

def reverse_string(s: str) -> str:
    """Reverses a string.

    Args:
        s (str): String.

    Returns:
        str: Reversed string.
    """
    return s[::-1]

def get_permutations(s: str) -> list:
    """Generates all possible permutations of a string.

    Args:
        s (str): A string containing some letters.

    Returns:
        list: A list with all possible permutations.
    """
    pass