a = int(input(' > '))
value = []

for i in range(1072, 1072 + a):
	value += list(chr(i))

print(value)