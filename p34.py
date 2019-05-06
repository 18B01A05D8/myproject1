def factorial(n):
	if n == 0 or n == 1:
		return 1

	else:
		return n * factorial(n-1)
sum1 = 0
for num in range(3,1000000):
        num1 = str(num)
        sum = 0
        for i in range(len(num1)):
                n = int(num1[i])
                sum += factorial(n)
        if sum == num:
                sum1 += sum
print(sum1)

