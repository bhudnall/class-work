def computepay(hours, rate):

	hours = float(hours)
	rate = float(rate)
	total = hours * rate

	extra_cash = 0
	if hours > 40:
		extra_hr = hours - 40
		time_half = extra_hr / 2
		extra_cash = time_half * rate

	return total + extra_cash

hr = raw_input("Enter Hours: ")
rt = raw_input("Enter Rate: ")

print "Pay: %f" % round(computepay(hr, rt), 2)

