days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # use "\n" to start on a new line
#  the \n newlines do not work when you use %r because that's how %r formatting works, it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.

print "Here are the days: ", days # use "," to concatenate string & variable
print "Here are the months: ", months

print """ 
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
# use """ (no space between them) to print multiple lines without repeating "print" on each line