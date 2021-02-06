# Qns 1
# Write a Python program to convert Degrees to Radians.
import math

def toradian(conv):
    return math.radians(conv)

deg = int(input("Enter Degrees: "))
print(toradian(deg))

