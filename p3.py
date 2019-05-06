def isprime(n):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0:
		return False

	r = 3
	while (r * r) <= n:
		if n % r == 0:
			return False
		r += 2
	return True

def factorisation(n):
	factor = 2
	factors = []

	while n > 2:
		if n % factor == 0:
			if isprime(factor):
				factors.append(factor)
				n //= factor
		factor += 1
	return factors

print(max(factorisation(600851475143)))

	
