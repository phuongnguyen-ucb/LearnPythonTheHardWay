x = "There are %d types of people." % 10 # %d is for number, %s for string, %r for anything

# Use the %r for debugging, since it displays the "raw" data of the variable (that's why it can be either number or string), but the others are used for displaying variables to users.

binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) 

print x
print y

print "I said: %r." % x #if I use %r, python automatically put a single quote around my string
print "I also said: '%s'." % y #if I use something else but %r, I have to type in a single quote around my string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # I get "Isn't that jose so funny?! False"
# I can get same result as above using: joke_evaluation = "Isn't that joke so funny?! %r" % hilarious => print joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

print w + e # use "+" to concatenate 2 variables