# Using range(1,50), make two lists, 
# one containing all even numbers and other containing all odd numbers.

odd = []
even = []

for i in range(1, 50):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"Even: {even}")
print(f"Odd: {odd}")