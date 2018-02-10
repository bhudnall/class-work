def computegrade(score):

	try:
		if float(score):
			score = float(score)
			if score > 1:
				raise ValueError
			elif score >= 0.9:
				grade = 'A'
			elif score >= 0.8:
				grade = 'B'
			elif score >= 0.7:
				grade = 'C'
			elif score >= 0.6:
				grade = 'D'
			else:
				grade = 'F'
			return grade

	except ValueError:
		return 'Bad Score'

score = raw_input("Enter score: ")
print computegrade(score)


