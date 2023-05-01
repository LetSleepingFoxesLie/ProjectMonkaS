from lsfm import is_even, generate_fibonacci_until_n

def main():
    
    # Generates Fibonacci numbers until 4 million
    fibonacci_numbers = generate_fibonacci_until_n(4000000)
    
    # The sum
    s = 0
    
    # Main loop
    for fib in fibonacci_numbers:
        if is_even(fib): s += fib
    
    print(s)

if __name__ == "__main__":
    main()