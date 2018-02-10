
#################################################
#												#
#				   ASSIGNMENT 4				    #
#												#	
#################################################

# CHAPTER 6

# exercise 1

fruit = 'banana'

index = len(fruit)

while index > 0:
	index = index - 1
	print fruit[index]

# exercise 2


#fruit[:], means to show the entire word and not limit what is shown.
#it will print 'banana'


# exercise 3

def count(word, letter_):

	count = 0 

	for letter in word: 
		if letter == letter_: 
			count = count + 1

	print 'There are %d \'%s\' in the word \'%s\'' % (count, letter_, word)

count('banana', 'a')

# exercise 4

word = 'banana'
letter = 'a'
print 'There are %d, %s\'s in %s' % (word.count(letter, 0, len(word)), letter, word)

# exercise 5

string = 'X-DSPAM-Confidence: 0.8475'
print float(string[string.find(': ')+1:len(string)])

# CHAPTER 7

# exercise 1

fname = input('Enter the file name: ') 

try: 

	fhand = open(fname) 

except: 

	print 'File cannot be opened: %s' % fname
	exit() 

for line in fhand: 
	print line.upper()



# exercise 2

fname = input('Enter the file name: ') 

try: 

	fhand = open(fname) 

except: 

	print 'File cannot be opened: %s' % fname
	exit() 

xsum = 0.0
xcount = 0.0
for line in fhand: 
	line = line.rstrip()
	if line.find('X-DSPAM-Confidence:') == 0:
		xsum = xsum + float(line[line.find(': ')+1:len(line)])
		xcount = xcount + 1

print 'Average spam confidence: %f' % (xsum/xcount)


# exercise 3

fname = input('Enter the file name: ') 

try: 

	fhand = open(fname) 

except (NameError, IOError): 

	print '%s IS NOT A REAL FILE, YOU CANNOT USE THIS PROGRAM EVER AGAIN!!' % fname
	exit() 

xsum = 0.0
xcount = 0.0
for line in fhand: 
	line = line.rstrip()
	if line.find('X-DSPAM-Confidence:') == 0:
		xsum = xsum + float(line[line.find(': ')+1:len(line)])
		xcount = xcount + 1

print 'Average spam confidence: %f' % (xsum/xcount)








