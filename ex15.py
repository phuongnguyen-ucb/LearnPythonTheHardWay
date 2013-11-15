from sys import argv # import argument variables

script, filename = argv # make script and filename become variabls

txt = open(filename) # open the file

print "Here's your file %r:" % filename
print txt.read() # read the file

txt.close() # close the file after you're done

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()