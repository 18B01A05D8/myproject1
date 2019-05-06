def pythagorean(i,j,k):
	if k ** 2 == j ** 2 + i ** 2:
		return True
for i in range(1,1000):
	for j in range(1,1000):
		for k in range(1,1000):
			if pythagorean(i,j,k):
				a,b,c = i,j,k
				break
print(a*b*c)
				
