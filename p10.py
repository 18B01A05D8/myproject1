def isprime(num):
	if num == 2 or num == 3:
		return True

	if num % 2 == 0:
		return False

	r = 3
	while r * r <= num:
		if num % r == 0:
			return False
		r += 2
	return True
sum = 0
for i in range(2,2000000):
	if isprime(i):
		sum += i
print(sum)
