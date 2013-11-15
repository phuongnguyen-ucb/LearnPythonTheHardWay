print "I am 6'2\" tall." # escape double-quote inside string
print 'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in." # use "\t" to do horizontal tab 
persian_cat = "I'm split\non a line." # use "\n" to start a new line
backslash_cat = "I'm \\ a \\ cat." # "double \\ only print 1 \

fat_cat = '''
I'll do a list:
\t* Cat food 
\t* Fishies
\t* Catnip\n\t* Grass
'''
# use "\t*" to have * (da^'u hoa thi.) on every new line
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Tiny piece of fun code to try out:
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i, # use "\r" to return