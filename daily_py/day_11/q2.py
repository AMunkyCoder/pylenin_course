# Write a Python program to take two int values from user and print greatest among them.

first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))

if first_num == second_num:
    print("They are the same")
else:
    if first_num > second_num:
        print("First is bigger: ", first_num)
    else:
        print("Second is bigger: ", second_num)