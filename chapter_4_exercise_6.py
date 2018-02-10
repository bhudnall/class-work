def computepay(hours, rate):

	max_hours = 40
	try:
		if float(hours):
			hours = float(hours)
		else:
			raise ValueError

		if float(rate):
			rate = float(rate)
			if hours > max_hours:
				total = ((hours - max_hours) * .5 * rate) + (hours * rate)
			else:
				total = hours * rate
		else:
			raise ValueError

		return total

	except ValueError:
		return 'Error, please enter numeric input'

hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
print computepay(hours, rate)