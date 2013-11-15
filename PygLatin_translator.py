# Pyg Latin Translator: to translate English to Latin. 
# If a word is a vowel, add "ay" to the end of a word. 
# If a word is a consonant, take the first letter of a word and put it to the end, then add "ay" to the end of a word.

# Welcome users:
print "Welcome to the Pyg Latin Translator!"

# Ask users to type in a word:
original = raw_input('Enter a word:')

# Assign "ay" to a variable pyg:
pyg = "ay"

# Check to see if the string is not empty and if string contains only alphabetical characters:
if len(original) > 0 and original.isalpha():
    word = original.lower() # to conver the string value to lowercase
    first = word[0] # to hold the first letter of a word
    # check to see if the first letter of a word is a vowel (start with "a,e,i,o,u"):
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
		new_word = word + pyg # if it's a vowel, add "ay" to the end of a word
		print new_word
    else:
		new_word = word[1:] + word[0] + pyg # if it's a consonant, add the first letter to the end of a word + "ay"
		print new_word
else:
    print 'empty'
    