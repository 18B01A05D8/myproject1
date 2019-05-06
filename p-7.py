list = []

for i in range(2,200000):
	c = 0
	for j in range(2,i):
		if i % j == 0:
			c += 1
	if c == 0:
		list.append(i)

print(list[10000])
		 
