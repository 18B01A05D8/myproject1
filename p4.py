def revs(num):
	num1 = str(num)

	if num1[::-1] == num1:
		return True
	return False

list = []
for i in range(100,1000):
	for j in range(100,1000):
		if revs(i * j):
			list.append(i * j)
print(max(list))
		
