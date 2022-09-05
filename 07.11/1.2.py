age = int(input('Введите свой возраст: '))

if age <= 13:
	print('Детство')
elif 14 <= age <= 24:
	print('Молодость')
elif 25 <= age <= 59:
	print('Зрелость')
elif age >= 60:
	print('Старость')