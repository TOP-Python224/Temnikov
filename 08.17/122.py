VOWELS = ('a', 'e', 'i', 'o', 'u')

word = ""
while True:
	word = input("Введите текст: ")
	# ИСПОЛЬЗОВАТЬ: имена переменных пишутся в нижнем_змеином_регистре
	word_list = word.lower().split()
	# ИСПОЛЬЗОВАТЬ: достаточно проверки на истинность
	if not word:
		break
	else:
		for word in word_list:
			if word[0] in VOWELS:
				word = word + "way"
				print(word)
			else:
				for letter in word:
					if letter in VOWELS:
						# ИСПРАВИТЬ: не стоит вызывать метод два раза, когда можно вызывать один раз и сохранить результат в переменную
						word = word[word.index(letter):] + word[:word.index(letter)] + "ay"
						print(word)
						break


# Введите текст: I have loved you all along
# iway
# avehay
# ovedlay
# ouyay
# allway
# alongway


# ИТОГ: хорошо — 4/5
