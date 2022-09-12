VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
punct_marks = (',', '.', '!', '?', ':', ';')

while True:
	text = input("Введите слово: ")
	wordList = text.split()
	piglist = []
	if text == "":
		break
	for word in wordList:
		if word[-1] in punct_marks:
			new_word = word[:-1]
		else:
			new_word = word
		piglist.append(new_word)
	i = 0
	m = 0
	for word in piglist:
		for letter in word:
			if word[0] in VOWELS:
				pig_word = word + "way"
				piglist[i] = pig_word.capitalize() if word[0].isupper() else pig_word.lower()
			else:
				for letter in word:
					if letter in VOWELS:
						pig_word = (word[word.index(letter):] + word[:word.index(letter)] + "ay")
						piglist[i] = pig_word.capitalize() if word[0].isupper() else pig_word.lower()
						break
		i += 1
	for item in wordList:
		if item[-1] in punct_marks:
			piglist[m] = piglist[m] + item[-1:]
		m += 1

	print(wordList)
	print(piglist)


# Результат:
# Введите слово: Contractions include: don’t, isn’t, and wouldn’t.

# ['Contractions', 'include:', 'don’t,', 'isn’t,', 'and', 'wouldn’t.']
# ['Ontractionscay', 'includeway:', 'on’tday,', 'isn’tway,', 'andway', 'ouldn’tway.']
