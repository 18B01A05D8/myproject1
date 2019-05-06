f1 = 1
f2 = 1
f = 0
count = 2

while f < 10 ** 1001:
	f = f1 + f2
	f1,f2 = f2,f
	f3 = str(f)
	if len(f3) == 1000:
		break
	count += 1
print(count+1)


