x1 = str(input(' > ')).lower()
y1 = int(input(' > '))
x2 = str(input(' > ')).lower()
y2 = int(input(' > '))

if (x1 in 'aceg' and y1 % 2 != 0) or (x1 in 'bdfh' and y1 % 2 == 0):
	chess_cage1 = 'black'
else:
	chess_cage1 = 'white'

if (x2 in 'aceg' and y2 % 2 != 0) or (x2 in 'bdfh' and y2 % 2 == 0):
	chess_cage2 = 'black'
else:
	chess_cage2 = 'white'

if chess_cage1 == chess_cage2:
	print('ДА')
else:
	print('НЕТ')