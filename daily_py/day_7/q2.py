# Write a Python program to remove duplicates from a list.

def rem_dupe(dupe_list):
    new_list = []
    for i in dupe_list:
        if i not in new_list:
            new_list.append(i)
        else:
            continue
    return new_list

if __name__ == '__main__':
    num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
    
    print(rem_dupe(num_list))