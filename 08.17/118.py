s = input("Введите строку:\n")
signs = ['.', ',', ':', ';', '!', '?']
words = s.lower().split()

# ИСПРАВИТЬ: используйте enumerate() и строковые методы по аналогии с предыдущей задачей
i = 0
for word in words:
	if word[-1] in signs:
		words[i] = word[:-1]
		word = words[i]
	i += 1

l = len(words)
# ИСПОЛЬЗОВАТЬ: можно проще — разверните получившийся список слов и сравните с исходным списком:
# words == words[::-1]
for i in range(l//2):
	if words[i] != words[-1-i]:
		print("Не палиндром")
# ИСПОЛЬЗОВАТЬ: вместо выхода из приложения лучше использовать break и else блок циклов
		break
else:
	print("Палиндром")


# Результат
# Введите строку:
# Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?
# Палидром

# Введите строку:
# Contractions include: don’t, isn’t, and wouldn’t
# Не палидром


# ИТОГ: хорошо — 3/4
