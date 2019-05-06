sum = 0
sum1 = 0
for num in range(2,10000000):
	num1 = str(num)
	sum = 0
	for i in range(len(num1)):
		n = int(num1[i])
		sum += n ** 5
	if sum == num:
		sum1 += sum
print(sum1)
