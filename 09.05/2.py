string = input(' > ')
binary = {'0', '1', 'b'}

if set(string).issubset(binary):
	print('ДА')
else:
	print('НЕТ')


# stdout:
#  > 0100101
# ДА

#  > b0110
# ДА

#  > 0b01001110
# ДА

#  > 0ac1201001
# НЕТ

#  > 123
# НЕТ


# ИТОГ: отлично — 3/3
