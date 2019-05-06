f1 = 1
f2 = 2
f = f1 + f2
sum = 2

while f < 4000000:
	f1 = f2
	f2 = f
	f = f1 + f2
	if f % 2 == 0:
		sum += f

print(sum)	
