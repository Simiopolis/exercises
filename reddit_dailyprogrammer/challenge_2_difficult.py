# Objective:
# Your mission is to create a stopwatch program. this program should have start,
# stop, and lap options, and it should write out to a file to be viewed later.
# Link: 
# http://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challeinge_2/
import datetime

print "This is a stop watch"

raw_input("When ready, type in any key to start: ")
start = datetime.datetime.now()
raw_input("When ready to stop, type in any key: ")
end = datetime.datetime.now()

print "time: " + str(end - start)
