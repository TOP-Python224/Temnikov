result = {}

def math(string: int | float) -> dict:
	"""Функция принимает на вход один аргумент: list, tuple или str, 
    содержащий только целые или вещественные числа.
    Функция возвращает отсортированный словарь для
    среднего арифметического, геометрического, квадратичного и гармонического значения аргументов."""
	if type(string) not in (str, list, tuple):
		return None

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
	garm = 0
	
	for num in string:
		if type(num) not in (int, float):
			return None
		else:
			arith += num
			geom *= num
			quad += num * num
			garm += 1 / num
        
	result['arithmetic'] = arith / l
	result['geometric'] = pow(geom, 1 / l)
	result['quadratic'] = pow(quad / l, 1 / 2)
	result['garmonic'] = l / garm

	sorted_result = sorted(result.items(), key=lambda i: i[1])
	sorted_result = dict(sorted_result)

	return(sorted_result)


print(math((1.0, 2, 'three', 4, 5)))
print(math({}))
print(math('1 2 three 4 5'))
print(math('1 2 3 4 5'))
print(math((1, 2, 3)))
print(math([1, 2, 3, 4, 5]))

# Результат:

# None
# None
# None
# {'garmonic': 2.18978102189781, 'geometric': 2.605171084697352, 'arithmetic': 3.0, 'quadratic': 3.3166247903554}
# {'garmonic': 1.6363636363636365, 'geometric': 1.8171205928321397, 'arithmetic': 2.0, 'quadratic': 2.160246899469287}
# {'garmonic': 2.18978102189781, 'geometric': 2.605171084697352, 'arithmetic': 3.0, 'quadratic': 3.3166247903554}