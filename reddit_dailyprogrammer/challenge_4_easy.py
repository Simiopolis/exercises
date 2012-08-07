# Objective:
# You're challenge for today is to create a random password generator!
# For extra credit, allow the user to specify the amount of passwords to 
# generate. For even more extra credit, allow the user to specify the length 
# of the strings he wants to generate!
# Link: http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/
import string
import random

def generate_pw(num):
	for i in range(num):
		print ''.join(random.choice(string.ascii_letters + 
			string.digits + '!@#$%^&*()~') for s in 
			range(random.randint(10, 15))) + '\n'


generate_pw(10)
