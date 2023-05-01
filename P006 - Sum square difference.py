from lsfm import sum_of_natural_numbers, sum_of_squared_numbers

def main():
    sum_of_the_squares = sum_of_squared_numbers(100)
    # print(sum_of_the_squares)
    square_of_the_sum = sum_of_natural_numbers(100) ** 2
    # print(square_of_the_sum)
    print(abs(sum_of_the_squares - square_of_the_sum))
    
if __name__ == "__main__":
    main()