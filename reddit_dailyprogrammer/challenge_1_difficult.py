# we all know the classic "guessing game" with higher or lower prompts. 
# lets do a role reversal; you create a program that will guess numbers 
# between 1-100, and respond appropriately based on whether users say that 
# the number is too high or too low. Try to make a program that can guess 
# your number based on user input and great code!
# Link: 
# http://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/
import random

roof_num=100
floor_num=1

while(1):
	num_guess = random.randint(floor_num,roof_num)
	is_right = raw_input("Is your number " + str(num_guess) + "? (type y/n)")
	if is_right is 'y':
		break
	else:
		is_high_or_low = raw_input(
			"Is the guess too high or low?(type h/l)")
		if is_high_or_low is 'h':
			roof_num = num_guess
		else:
			floor_num = num_guess

print "Your number is " + str(num_guess)
