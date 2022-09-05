s = input()
ind = s.find('@')

if ind == -1 or s[ind + 1:].find('.') == -1:
	print('Неверно')
else:
	print('Верно')