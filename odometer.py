def validity(num):
	read = str(num)
	if num % 10 == 0 or num < 12 or int(read[1]) <= int(read[0]) or num > 99:
		return False
	return True



read1 = int(input('meter reading : '))
read = str(read1)
if read1 % 10 == 0 or read1 < 12 or int(read[1]) <= int(read[0]) or read1 > 99:
	print('invalid')
else:
	if validity(read1 - 1) == True:
		print('Previous Reading = ',read1 - 1)
	else:
		r = (int(read[0])-1)*10 + 9
		if r <= 9:
			print('Previous Reading = 89')
		else:
			print('Previous Reading = ',r)
	if validity(read1 + 1) == True:
		print('Next Reading = ',read1 + 1)
	else:
		w = (int(read[0])+1)*10 + (int(read[0])+2)
		if w >= 90:
			print('Next Reading = 12')
		else:
			print("Next Reading = ",w)

