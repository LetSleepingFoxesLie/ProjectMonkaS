def main():
    
    # Let's try something hacky to go O(n^2) instead of O(n^3), shall we?
    # Using Euclid's formula
    # If m > n > 0, then
    # a = m^2 - n^2, b = 2mn, c = m^2 + n^2
    # Once we find m, n so that 1000 mod (a + b + c) == 0, then let k = 1000 / (a + b + c). We want abck^3
    
    k = 0
    for n in range(1, 1000):
        for m in range(n, 1000):
            if m ** 2 + m * n >= 500:
                break
        
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            
            # If either value is zero, then continue into the next iteration
            if a * b * c == 0:
                continue
            
            if 1000 % (a + b + c) == 0:
                k = 1000 // (a + b + c)
                print(f"{a} * {b} * {c} * {k}^3 = {a * b * c * (k ** 3)}")
    
    
    # m^2 - n^2 + 2mn + m^2 + n^2 = 2m^2 + 2mn <= 1000 -> m^2 + mn <= 500
    pass

def very_inefficient_shit():
    for a in range(1, 999):
        for b in range(a, 999):
            for c in range(b, 999):
                print(f"{a} {b} {c}")
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    print(a * b * c)

if __name__ == "__main__":
    main()