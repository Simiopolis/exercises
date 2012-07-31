# Objective:
# Hello, coders! An important part of programming is being able to apply your 
# programs, so your challenge for today is to create a calculator application 
# that has use in your life. It might be an interest calculator, or it might be
# something that you can use in the classroom. For example, if you were in 
# physics class, you might want to make a F = M * A calc.
# Link: http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

# Not taking any courses that require a calculator right now, but I'll do the
# F = M * A

mass = raw_input("Please input the mass(kg): ")
acceleration = raw_input("Please input the acceleration(m/s): ")

force = float(mass) * float(acceleration)

print "-----------log----------"
print "mass: " + mass
print "acceleation: " + acceleration
print "Calculation: "
print "             " + mass + " kg * " + acceleration + " m/s = " + str(force) + " N"
print "Force: " + str(force)
