from random import randrange as rr


def del_min_max_values(
		# Известно понимание передаваемого параметра
		data: list,
		n: int,
		*,
		upd: bool
# Для простоты понимания кода
) -> None | list:
	"""Функция, которая удаляет n минимальных и n максимальных значений из списка чисел."""
	
	if upd:
		for num in range(n):
			data.remove(min(data))
			data.remove(max(data))
		return None
	else:
		new_data = data.copy()
		for num in range(n):
			new_data.remove(min(new_data))
			new_data.remove(max(new_data))
		return new_data


print(del_min_max_values(
	[rr(-100, 100) for _ in range(10)],
	2,
	upd=True
))
print(del_min_max_values([rr(-100, 100) for _ in range(15)], 4, upd=False))
print(del_min_max_values([rr(-100, 100) for _ in range(20)], n=6, upd=False))
print(del_min_max_values([rr(-100, 100) for _ in range(25)], 8, False))


# stdout

# None
# [44, -29, -6, -4, 21, 11, -13]
# [-27, -18, 52, -21, 1, 0, 4, 51]
# Traceback (most recent call last):
#   File "D:\!PYTHON\Python\GitHub_HW\Temnikov\08.24\3.py", line 30, in <module>
#     print(del_min_max_values([rr(-100, 100) for _ in range(25)], 8, False))
# TypeError: del_min_max_values() takes 2 positional arguments but 3 were given
