scores = []
while True:
	try:
		score = raw_input("Enter a number: ")
		if score.strip() == "done":
			break
		elif float(score):
			scores.append(float(score))
		else:
			raise ValueError
	except ValueError:
		print "Invalid input"

if len(scores) > 0:
	print "Total: %d, Count: %d, Average: %f" % (sum(scores),
												 len(scores), 
												 (sum(scores)/len(scores)))
