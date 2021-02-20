# Write a Python program to build a list containing 5 integer zeros.

def create_list():
    zero_list = []
    for i in range(1, 6):
        zero_list.append(0)
        print(i)
    return zero_list

if __name__ == '__main__':
    print(create_list())