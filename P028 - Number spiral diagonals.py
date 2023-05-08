from lsfm import is_even

def main():
    print(get_spiral_sum(1001))

# A bit messy, but it works
def get_spiral_sum(grid_size: int) -> int:
    s = 1
    if is_even(grid_size):
        return s
    
    iterations = grid_size // 2
    for i in range(1, iterations + 1):
        s += (4 * ((2 * i + 1) ** 2)) - 12 * i
    
    return s
        
        
if __name__ == "__main__":
    main()