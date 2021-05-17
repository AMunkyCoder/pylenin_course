# A school follows the following grading system:

#     Below 25 - F
#     25 to 45 - E
#     45 to 50 - D
#     50 to 60 - C
#     60 to 80 - B
#     Above 80 - A

# Ask user to enter marks and print the corresponding grade.

grade = int(input("Enter your grade: "))

if grade > 80:
    print("Your mark is A")
elif grade >= 60:
    print("Your mark is B")
elif grade >= 50:
    print("Your mark is C")
elif grade >= 45:
    print("Your mark is D")
elif grade >= 25:
    print("Your mark is E")
elif grade < 25:
    print("Your mark is F")