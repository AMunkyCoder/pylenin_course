# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
# Write a Python program, 
# asking user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter Salary: "))
years_of_service = int(input("Enter Years of Service: "))


if years_of_service >= 5:
    net_bonus = (salary * .05)
else:
    net_bonus = 0

print("Your bonus is:", net_bonus)