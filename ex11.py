print "How old are you?",
age = raw_input() # Whatever I type in, it's a string. Even I type in number, it's still a string
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Way 2 to do raw_input:
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)