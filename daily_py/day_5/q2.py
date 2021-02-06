# Qns 2
# Write a Python program to check if any of the variables below are Integer types.

# x = "Pylenin"
# y = 7
# z = abs(-22)

x = "Pylenin"
y = 7
z = abs(-22)

check_list = [x, y, z]

for l in check_list:
    if isinstance(l, int):
        print("{} is an Integer.".format(l))