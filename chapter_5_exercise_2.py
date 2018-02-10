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
	print "Max: %f, Min: %f" % (max(scores), min(scores))
