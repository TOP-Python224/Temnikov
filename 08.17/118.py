s = input("Введите строку:\n")
signs = ['.', ',', ':', ';', '!', '?']
words = s.lower().split()

i = 0
for word in words:
	if word[-1] in signs:
		words[i] = word[:-1]
		word = words[i]
	i += 1

l = len(words)

for i in range(l//2):
	if words[i] != words[-1- i]:
		print("Не палидром")
		quit()

print("Палидром") 

# Результат
# Введите строку:
# Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?

# Палидром

# Введите строку:
# Contractions include: don’t, isn’t, and wouldn’t

# Не палидром