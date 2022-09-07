from typing import SupportsFloat

result = {}

# ИСПРАВИТЬ: все имена должны быть значащими — что такое math, как соответствует string заявленному типу?
# ИСПОЛЬЗОВАТЬ: в ситуации, когда у нас заданы определённое количество типов, и нам необходимо их перечислить в аннотации, то для этого можно создать отдельную переменную:
NumSeqType = list[SupportsFloat] | tuple[SupportsFloat, ...] | str
# ИСПОЛЬЗОВАТЬ: для словаря можно также уточнить тип ключей и значений:
def math(string: NumSeqType) -> dict[str, float]:
	# ИСПРАВИТЬ: перепишите описание функции по аналогии с задачей 91 — можно без подробного описания параметров и возвращаемого значения, главное, первую строку документации
	"""Функция принимает на вход один аргумент: list, tuple или str, содержащий только целые или вещественные числа. Функция возвращает отсортированный словарь для среднего арифметического, геометрического, квадратичного и гармонического значения аргументов."""
	# ИСПОЛЬЗОВАТЬ: встроенная функция isinstance() больше подходит для таких проверок
	if not isinstance(string, (str, list, tuple)):
		# ИСПОЛЬЗОВАТЬ: здесь лучше выбросить исключение
		raise TypeError('сообщение об ошибке типа')

	# ОТВЕТИТЬ: а нужно ли здесь перехватывать исключения? в коде верхнего уровня вы нигде не проверяете возвращаемое значение на None => оно не используется => лучше выбросить исключение
	try:
		# ИСПОЛЬЗОВАТЬ: функция type() возвращает объект класса, поэтому с ней мы используем оператор is
		if type(string) is str:
			res = []
			for item in string.rstrip().split():
				item = float(item)
				res.append(item)
				string = res
	except ValueError:
		return None

	l = len(string)
	arith = 0
	geom = 1
	quad = 0
	harm = 0
	
	for num in string:
		# ИСПОЛЬЗОВАТЬ: встроенная функция isinstance() больше подходит для таких проверок
		if not isinstance(num, SupportsFloat):
			# ИСПОЛЬЗОВАТЬ: здесь лучше выбросить исключение
			raise TypeError('сообщение об ошибке типа')
		else:
			# КОММЕНТАРИЙ: а вот это хороший заход, за один цикл вычислить все последовательности — хвалю!
			arith += num
			geom *= num
			quad += num * num
			harm += 1 / num

	result['arithmetic'] = arith / l
	result['geometric'] = pow(geom, 1/l)
	result['quadratic'] = pow(quad/l, 1/2)
	result['harmonic'] = l / harm

	sorted_result = sorted(result.items(), key=lambda i: i[1])
	sorted_result = dict(sorted_result)

	# ИСПОЛЬЗОВАТЬ: выражение возвращаемого значения берётся в круглые скобки только если его необходимо перенести на новую строку
	return sorted_result


# print(math((1.0, 2, 'three', 4, 5)))
# print(math({}))
# print(math('1 2 three 4 5'))
print(math('1 2 3 4 5'))
print(math((1, 2, 3)))
print(math([1, 2, 3, 4, 5.9]))


# stdout:
# None
# None
# None
# {'garmonic': 2.18978102189781, 'geometric': 2.605171084697352, 'arithmetic': 3.0, 'quadratic': 3.3166247903554}
# {'garmonic': 1.6363636363636365, 'geometric': 1.8171205928321397, 'arithmetic': 2.0, 'quadratic': 2.160246899469287}
# {'garmonic': 2.18978102189781, 'geometric': 2.605171084697352, 'arithmetic': 3.0, 'quadratic': 3.3166247903554}


# ИТОГ: хорошо — 4/5
