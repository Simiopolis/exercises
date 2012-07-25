# Problem found on reddit/r/programingchallenges
# Objective: Print 1 22 333 4444 ... up to 9
# Link: http://www.reddit.com/r/programingchallenges/comments/s8awi/beginners_homework_assignmentpython/ 

# What I did
def print_(num):
    if num == 0:
	return
    for i in range(1,num+1):
	for n in range(0,i):
	    print i,
        print "\n"

# Better way, maybe? (Edited from a reddit comment)
def better_print_(num):
    for i in [(str(x)*x) for x in range(1, num+1)]:
	print i

print_(9)
better_print_(9)
