# Write a Python program to find the largest number in a list.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest_number = 0

for i in x:
    if i > largest_number:
        largest_number = i

print(largest_number)

# or 

print(max(x))