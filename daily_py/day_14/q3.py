# Write a Python program to construct the following pattern.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
a = 5

for i in range(1, a + 1):
    print(i* "* ")
for i in range(a-1, 0, -1):
    print(i* "* ")