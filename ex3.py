# Enter a random number and guess it until succeed
# Author: Xuanru Guo
# using random

import random
# a random number between 10 and 20
number = random.randint(10,20)

print("This is the random number: ", number)

# a flag whether the guess is right
found = 0
guess = int(input("Guess a number: "))

while found == 0:
	if guess == number:
		print("Congratulations!")
		found = 1
	else:
		guess = int(input("Sorry. Enter number again: "))


