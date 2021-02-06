# Qns 4
# Write a Python program which accepts the user’s first and last name 
# and print them in reverse order with a space between them.

def reverse(name):
    return name[::-1]


name = str(input("Enter Name: "))
print(reverse(name))