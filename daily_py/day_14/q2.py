# Write a Python program that prints all the numbers 
# from 0 to 10 except multiples of 3 (use continue).

for i in range(10):
    if i % 3 == 0:
        continue
    else:
        print(i)