VOWELS = ('a', 'e', 'i', 'o', 'u')

word = ""

while True:
	word = input("Введите текст: ")
	wordList = word.lower().split()
	if word == "":
		break
	else:
		for word in wordList:
			if (word[0] in VOWELS):
				word = word + "way"
				print(word)
			else:
				for letter in word:
					if letter in VOWELS:
						word = (word[word.index(letter):] + word[:word.index(letter)] + "ay")
						print(word)
						break

# Введите текст: I have loved you all along

# iway
# avehay
# ovedlay
# ouyay
# allway
# alongway