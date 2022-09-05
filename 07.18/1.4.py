a = [int(i) for i in input()]

if sum(a[:3]) == sum(a[3:]):
	print('ДА')
else:
	print('НЕТ')