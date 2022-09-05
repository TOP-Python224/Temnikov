x1 = str(input(' > ')).lower()
y1 = int(input(' > '))
x2 = str(input(' > ')).lower()
y2 = int(input(' > '))

desk = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

if abs(desk.get(x1) - desk.get(x2)) <= 1 and abs(y1 - y2) <= 1:
	print('ДА')
else:
	print('НЕТ') 