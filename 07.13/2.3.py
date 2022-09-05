s = 0

for num in range(100, 9999):
	if  num % 10 != num // 100 and num %10 != num // 10 % 10 and num // 10 % 10 != num // 100 and num % 10 != 0:
		s += 1

print(s)