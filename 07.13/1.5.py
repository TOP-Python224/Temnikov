result = ''

while True:
	n = int(input(' > '))
	result = (f'{result} {n}')
	if n % 7 != 0:
		print(f'{result}', end=' ')
		break