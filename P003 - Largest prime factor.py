from lsfm import generate_prime_factors

def main():
    prime_decomposition = generate_prime_factors(600851475143)
    print(max(prime_decomposition))

if __name__ == "__main__":
    main()