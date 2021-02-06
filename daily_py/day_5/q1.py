# Qns 1
# Write a Python Program to check if a number is odd or even.

def checker(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
num = int(input("Enter Number: "))
checker(num)