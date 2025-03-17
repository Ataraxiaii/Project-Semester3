# Enter an age and inform quality for discounts
# Author: Xuanru Guo
# using if...else

# prompt the user for age
age = int(input("Please enter your age: "))

# decide which type of discounts the user has
if age <= 19:
	print("You qualify for student discounts.")
elif 20 <= age <= 54:
	print("You qualify for no age discounts.")
else: 
	print("You can receive senior discounts.")
