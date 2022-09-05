s = input()
price = 0.80
text = ''

for i in s:
	if i not in ' ':
		text += i

lenght = len(text)
sum = (lenght * price) * 100

print(f'{int(sum // 100)} руб. {int(sum % 100)} коп.')
