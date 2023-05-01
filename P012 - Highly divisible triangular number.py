# I apparently have already solved this one... lol
from lsfm import count_divisors, nth_triangular_number

# Kind of not so efficient, but works! Takes around a second, but most high-level code would take less than 100ms :/
def inefficient_approach():
    iterator = 1
    while True:
        triangular_number = nth_triangular_number(iterator)
        print(triangular_number)
        if count_divisors(triangular_number) >= 500:
            print(f"Triangular number #{iterator} = {triangular_number}")
            break
        else:
            iterator += 1

if __name__ == "__main__":
    inefficient_approach()