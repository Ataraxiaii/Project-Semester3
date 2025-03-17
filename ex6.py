# Enter a number and calculate the factorial of it
# Author: Xuanru Guo
# Using for loop

# define a function
def factorial(num):
	result = 1
	for i in range(1, num+1):
		result *= i
	return result

# enter the number
num = int(input("Please enter a number: "))
fact = factorial(num)
# output
print(f"The factorial of {num} is {fact}.")
