def factorial(n):
	p = 1
	for i in range(1,n+1):
		p *= i
	return p

n = factorial(100)
sum1 = 0
n1 = str(n)
for i in range(len(n1)):
        sum1 += int(n1[i])
print(sum1)

