
#################################################
#												#
#				   ASSIGNMENT 5				    #
#												#	
#################################################

# CHAPTER 8

# Exercise 1: Write a function called chop that takes a list and 
# modifies it, removing the first and last elements, and returns 
# None. Then write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements.

def chop(ls):

	del ls[0]
	del ls[len(ls) - 1]

	return ls

print chop([1, 2, 3, 4, 5, 6])


# Exercise 2: Figure out which line of the above program is still not 
# properly guarded. See if you can construct a text file which causes 
# the program to fail and then modify the program so that the line is 
# properly guarded and test it to make sure it handles your new text file.


fhand = open('mbox-short-2.txt') 
count = 0 
for line in fhand: 
	words = line.split() 
	# print 'Debug:', words 
	if len(words) < 3: continue 
	if words[0] != 'From': continue
	print words[2]

# Exercise 3: Rewrite the guardian code in the above example without two if statements. 
# Instead, use a compound logical expression using the and logical operator with 
# a single if statement.

fhand = open('mbox-short-2.txt') 
count = 0 
for line in fhand: 
	words = line.split() 
	# print 'Debug:', words 
	if len(words) > 3 and words[0] == 'From':
		print words[2]

# Exercise 4

fi = raw_input('Enter file: ') 
fhand = open(fi)
word_ls = []
for line in fhand: 
	words = line.split() 
	# print 'Debug:', words 
	for word in words:
		if word not in word_ls:
			word_ls.append(word)

print sorted(word_ls)

# Exercise 5: Write a program to read through the mail box data and when you 
# find line that starts with "From", you will split the line into words using 
# the split function. We are interested in who sent the message, which is 
# the second word on the From line.


fi = raw_input('Enter file: ') 
fhand = open(fi)
count = 0 
for line in fhand: 
	words = line.split() 
	if len(words) > 3 and words[0] == 'From':
		count += 1
		print words[1]

print 'There were %d lines in the file with From as the first word' % count



# Exercise 6: Rewrite the program that prompts the user for a list of numbers 
# and prints out the maximum and minimum of the numbers at the end when the 
# user enters "done". Write the program to store the numbers the user enters 
# in a list and use the max() and min() functions to compute the maximum and 
# minimum numbers after the loop completes.



num_list = []
while True:
	temp_num = raw_input("Enter a number: ")
	if temp_num.strip() == 'done':
		break
	if int(temp_num):
		num_list.append(int(temp_num))

if len(num_list): 
	print 'Maximum: ', max(num_list)
	print 'Minimum: ', min(num_list)

# CHAPTER 9

# Exercise 1: [wordlist2] Write a program that reads the words in words.txt 
# and stores them as keys in a dictionary. It doesn't matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string 
# is in the dictionary.

mydict = {}
fi = raw_input('Enter file: ') 
fhand = open(fi)
for word in fhand:
	if word not in mydict.keys():
		temp_word = word.rstrip()
		mydict[temp_word] = temp_word

print mydict

# Exercise 2: Write a program that categorizes each mail message by which day of 
# the week the commit was done. To do this look for lines that start with "From", 
# then look for the third word and keep a running count of each of the days of 
# the week. At the end of the program print out the contents of your dictionary 
# (order does not matter).


mydict = {}
fi = raw_input('Enter file: ') 
fhand = open(fi)
for line in fhand: 
	words = line.split() 
	if len(words) < 3: continue 
	if words[0] != 'From': continue
	if words[2] not in mydict.keys():
		mydict[words[2]] = 1
	else:
		mydict[words[2]] += 1

print mydict

# Exercise 3: Write a program to read through a mail log, build a histogram 
# using a dictionary to count how many messages have come from each email 
# address, and print the dictionary.


mydict = {}
fi = raw_input('Enter file: ') 
fhand = open(fi)
for line in fhand: 
	words = line.split() 
	if len(words) < 3: continue 
	if words[0] != 'From': continue
	if words[1] not in mydict.keys():
		mydict[words[1]] = 1
	else:
		mydict[words[1]] += 1

print mydict


# Exercise 4: Add code to the above program to figure out who has the most 
# messages in the file. After all the data has been read and the dictionary 
# has been created, look through the dictionary using a maximum loop (see 
# Section [maximumloop]) to find who has the most messages and print how 
# many messages the person has.

mydict = {}
fi = raw_input('Enter file: ') 
fhand = open(fi)
for line in fhand: 
	words = line.split() 
	if len(words) < 3: continue 
	if words[0] != 'From': continue
	if words[1] not in mydict.keys():
		mydict[words[1]] = 1
	else:
		mydict[words[1]] += 1

print max(mydict, key=mydict.get), mydict[max(mydict, key=mydict.get)]


# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from 
# (i.e., the whole email address). At the end of the program, print 
# out the contents of your dictionary.

mydict = {}
fi = raw_input('Enter file: ') 
fhand = open(fi)
for line in fhand: 
	words = line.split() 
	if len(words) < 3: continue 
	if words[0] != 'From': continue
	address = words[1][words[1].find('@')+1:len(words[1])] 
	if address not in mydict.keys():
		mydict[address] = 1
	else:
		mydict[address] += 1

print mydict


# CHAPTER 10

# Exercise 1: Revise a previous program as follows: Read and parse the "From" 
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary. After all the data has been read, print 
# the person with the most commits by creating a list of (count, email) tuples 
# from the dictionary. Then sort the list in reverse order and print out the 
# person who has the most commits.


mydict = {}
mytups = []
fi = raw_input('Enter file: ') 
fhand = open(fi)
for line in fhand: 
	words = line.split() 
	if len(words) < 3: continue 
	if words[0] != 'From': continue
	if words[1] not in mydict.keys():
		mydict[words[1]] = 1
	else:
		mydict[words[1]] += 1

for key, value in mydict.iteritems():
	mytups.append((value, key))

max_emails = sorted(mytups, reverse=True)[0]

print max_emails[1], max_emails[0]

# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the "From" line 
# by finding the time string and then splitting that string into 
# parts using the colon character. Once you have accumulated the counts
# for each hour, print out the counts, one per line, sorted by hour 
# as shown below.



mydict = {}
mytups = []
fi = raw_input('Enter file: ') 
fhand = open(fi)
for line in fhand: 
	words = line.split() 
	if len(words) < 3: continue 
	if words[0] != 'From': continue
	hour = words[5].split(':')[0]
	if hour not in mydict.keys():
		mydict[hour] = 1
	else:
		mydict[hour] += 1

for key, value in mydict.iteritems():
	mytups.append((key, value))

hr_counts = sorted(mytups)

for hr in hr_counts:
	print hr[0], hr[1]

# Exercise 3: Write a program that reads a file and prints the letters 
# in decreasing order of frequency. Your program should convert all 
# the input to lower case and only count the letters a-z. Your program 
# should not count spaces, digits, punctuation, or anything other than 
# the letters a-z. Find text samples from several different languages and 
# see how letter frequency varies between languages. Compare your results 
# with the tables at wikipedia.org/ wiki/ Letter_frequencies.


mydict = {}
mytups = []
fi = raw_input('Enter file: ') 
fhand = open(fi)
for line in fhand: 
	words = line.split()
	for word in words:
		for lett in word:
			if lett.isalpha():
				l = lett.lower()
				if l not in mydict.keys():
					mydict[l] = 1
				else:
					mydict[l] += 1

for key, val in mydict.iteritems():
	mytups.append((val, key))

let_counts = sorted(mytups, reverse=True)

for let in let_counts:
	print let[1], let[0]



















