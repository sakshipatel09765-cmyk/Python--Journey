# Write a program that takes total bill amount and number of friends as input calculate how much each person will pay. Also print data type of each variable.

total_bill = float(input("Enter Total bill amount: "))
num = int(input("Enter number of friends: "))

# implicit type conversion

amount_per_person = total_bill / num

print("Each will pay:", amount_per_person)
print("Data type of total_bill:", type(total_bill))
print("Data type of num:", type(num))
print("Data type of amount_per_person:", type(amount_per_person))