# Write a Python program to get the largest number from a list.

def get_highest(highest_list):
    base = 0
    for num in highest_list:
        if base < num:
            base = num
    return base


if __name__ == '__main__':
    num_list = [101, 1, 2, 3, 4, 5, 6, 7, 1001, 8, 9, 100]
    print(get_highest(num_list))
    
    print(max(num_list))