result = {}

def math(string: int | float, *args) -> dict:
	"""Функция принимает на вход один аргумент: list, tuple или str, содержащий только целые или вещественные числа. Функция возвращает отсортированный словарь для среднего арифметического, геометрического, квадратичного и гармонического значения аргументов."""
	if type(string) not in (str, list, tuple, int, float):
		return None

	if len(args) != 0:
		string = [string] + [item for item in args]

	try:
		if type(string) == str:
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
		if type(num) not in (int, float):
			return None
		else:
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

	return sorted_result


print(math([1, 2, 3, 4.23]))
print(math(-1, 1.5, -2, 2.5))
print(math('0.2 0.12 1'))
print(math('0b010 0b110'))
print(math(1, 2, '3 4'))
print(math([1, 2], '3 4'))


# stdout:

# {'garmonic': 1.9326099371787548, 'geometric': 2.244517027586113, 'arithmetic': 2.5575, 'quadratic': 2.823689961734468}
# {'garmonic': -9.23076923076923, 'arithmetic': 0.25, 'geometric': 1.6548754598234365, 'quadratic': 1.8371173070873836}
# {'garmonic': 0.20930232558139533, 'geometric': 0.2884499140614817, 'arithmetic': 0.44, 'quadratic': 0.5928462420110856}
# None
# None
# None
