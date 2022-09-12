string = input("Введите текст: \n")
signs = ['.', ',', ':', ';', '!', '?']

words = string.split()

i = 0
for word in words:
	if word[-1] in signs:
		words[i] = word[:-1]
		word = words[i]
	i += 1
print(words)


# Результат:
# Введите текст:
# Contractions include: don’t, isn’t, and wouldn’t.
# ['Contractions', 'include', 'don’t', 'isn’t', 'and', 'wouldn’t']
