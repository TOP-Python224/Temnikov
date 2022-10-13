items = []
result = ''

# ИСПРАВИТЬ: на любой вариант реализации цикла while без дублирования кода
line = input("Введите слово: ")
while line != "":
	items.append(line)
	line = input("Введите слово: ")

if len(items) == 0:
	print('<пусто>')
elif len(items) == 1:
	print(str(items[0]))
else:
	# ИСПРАВИТЬ: строковый метод join()
	for i in range(0, len(items) - 2):
		result = result + str(items[i]) + ", "

	result = result + str(items[len(items)-2]) + " и "
	result = result + str(items[len(items)-1])

	print(result)


# Результат
# Введите слово: лимон
# Введите слово: банан
# Введите слово: апельсин
# Введите слово:
# лимон, банан и апельсин


# ИТОГ: не использованы строковые методы — 2/5
