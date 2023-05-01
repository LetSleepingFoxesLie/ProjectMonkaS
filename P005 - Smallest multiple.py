def main():
    print(smallest_multiple(20))

def smallest_multiple(n: int) -> int:
    numbers = [i + 1 for i in range(0, n)]
    div = 2
    number = 1
    
    while True:
        
        # The program will be done once the product of all numbers in the list is equal to 1
        loop_stopper = 1
        
        # Checks whether anything was divided in this iteration
        has_divided_this_iteration = False
        
        # For each number in the list...
        for n in range(len(numbers)):
            
            loop_stopper *= numbers[n]
            
            # check if our current divisor divids it...
            if numbers[n] % div == 0:
                
                # and, if it does, divide it, and make it aware something was divided this iteration
                numbers[n] //= div
                has_divided_this_iteration = True
            
        # If everything in this list is equal to one, then we have the number
        if loop_stopper == 1:
            return number
            
        # Otherwise, update number and divisor
        if has_divided_this_iteration:
            number *= div
        else:
            div += 1
        
if __name__ == "__main__":
    main()