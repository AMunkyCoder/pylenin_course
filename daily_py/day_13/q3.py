# Write a program to find the greatest common divisor (GCD) 
# or highest common factor (HCF) of two numbers.


def get_smallest_and_largest_number(num1, num2):
    if num1 < num2:
        smallest_num = num1
        largest_num = num2
    else:
        smallest_num = num2
        largest_num = num1
    return smallest_num, largest_num


def get_factors(num):

    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    
    return factors


def get_hcf(largest_number, factors):
    hcf = []
    for factor in factors:
        if largest_number % factor == 0:
            hcf.append(factor)
    return max(hcf)

def main():
    first_num = 8
    second_num = 20

    smallest_num, largest_number = get_smallest_and_largest_number(first_num, second_num)
    
    factors = get_factors(smallest_num)
    
    hcf = get_hcf(largest_number, factors)
    
    print("The Smallest Number is: ", smallest_num)
    print("The Biggest Number is: ", largest_number)
    print("The Factors are: ", factors)
    print("The HCF is: ", hcf)
    

if __name__ == '__main__':
    main()