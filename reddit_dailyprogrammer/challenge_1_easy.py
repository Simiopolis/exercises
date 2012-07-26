# Objective:  
# create a program that will ask the users name, age, and reddit username. 
# have it tell them the information back, in the format:
#	your name is (blank), you are (blank) years old, and your username 
#	is (blank)
#	for extra credit, have the program log this information in a file 
#	to be accessed later.
# Link: http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/ 
name = raw_input("What is your name?\n")
age = raw_input("What is your age?\n")
username = raw_input("What is your username?\n")
print "\n\n"

text = "Your name is {0}, you are {1} years old, and your username is {2}.".format(
	name,age,username)
print text

f = open('challenge_1_log.txt','w')
f.write(text)
f.close()
