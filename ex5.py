# define a function that enters the factotial of entered number
# Author: Xuanru Guo
# using a function

# define the function
def factorial(num):
	result = 1
	while num > 0:
		result *= num
		num -= 1
	return result

# enter a number
num = int(input("Please enter a number: "))
# output
# print the factorial of entered number
print("The factorial of entered number is: ")
print(factorial(num))
