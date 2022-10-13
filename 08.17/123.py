VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
# КОММЕНТАРИЙ: есть ещё кавычки (три распространённых вида, и ещё семь–восемь редких), апострофы, дефисы и пропасть других знаков препинания
# КОММЕНТАРИЙ: эта проблема однозначно решается только вычислением в строке всех символов, не являющихся буквами и символами пространства — можно строковыми методами, можно множествами
punct_marks = (',', '.', '!', '?', ':', ';')

while True:
	text = input("Введите слово: ")
	word_list = text.split()
	pig_list = []
	if text == "":
		break
	for word in word_list:
		# ИСПРАВИТЬ: а если в конце слова будет несколько знаков препинания? (см. тесты ниже)
		if word[-1] in punct_marks:
			new_word = word[:-1]
		else:
			new_word = word
		pig_list.append(new_word)
	# ИСПОЛЬЗОВАТЬ: встроенную функцию enumerate()
	i = 0
	m = 0
	for word in pig_list:
		# УДАЛИТЬ: а этот цикл здесь зачем?
		for letter in word:
			if word[0] in VOWELS:
				pig_word = word + "way"
				pig_list[i] = pig_word.capitalize() if word[0].isupper() else pig_word.lower()
			else:
				for letter in word:
					if letter in VOWELS:
						pig_word = word[word.index(letter):] + word[:word.index(letter)] + "ay"
						pig_list[i] = pig_word.capitalize() if word[0].isupper() else pig_word.lower()
						break
		i += 1
	for item in word_list:
		if item[-1] in punct_marks:
			pig_list[m] = pig_list[m] + item[-1:]
		m += 1

	print(word_list)
	print(pig_list)


# Результат:
# Введите слово: Contractions include: don’t, isn’t, and wouldn’t.
# ['Contractions', 'include:', 'don’t,', 'isn’t,', 'and', 'wouldn’t.']
# ['Ontractionscay', 'includeway:', 'on’tday,', 'isn’tway,', 'andway', 'ouldn’tway.']

# СДЕЛАТЬ: обязательно проводите несколько тестов для разных входных данных
# Введите слово: What did he say?! "Be gone", — that's the quote.
# ['What', 'did', 'he', 'say?!', '"Be', 'gone",', '—', "that's", 'the', 'quote.']
# ['Atwhay', 'idday', 'ehay', 'ay?say!', 'e"bay', 'one"gay,', '—', "at'sthay", 'ethay', 'uoteqay.']

# "Fritz & Thompson" was written on the bronze label near the door.
# ['"Fritz', '&', 'Thompson"', 'was', 'written', 'on', 'the', 'bronze', 'label', 'near', 'the', 'door.']
# ['itz"fray', '&', 'Ompson"thay', 'asway', 'ittenwray', 'onway', 'ethay', 'onzebray', 'abellay', 'earnay', 'ethay', 'oorday.']


# ИТОГ: доработать — 3/6
