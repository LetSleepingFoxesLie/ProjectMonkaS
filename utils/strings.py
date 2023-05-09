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