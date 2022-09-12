# КОММЕНТАРИЙ: см. правки и комментарии к самой функции в задаче 5 задания 08.22

from numbers import Real

result = {}


# ИСПОЛЬЗОВАТЬ: если вы располагаете параметр string на первой позиции, то согласно условию он должен иметь возможность принимать как числовой объект, так и итерируемый объект, содержащий числа — и мы должны это проверить в теле функции
NumSeq = list[Real] | tuple[Real, ...] | str
# ИСПОЛЬЗОВАТЬ: а для параметра args мы можем сразу писать аннотацию типов аргументов
# ИСПОЛЬЗОВАТЬ: для словаря можно также уточнить тип ключей и значений:
def math(string: NumSeq | Real, *args: Real) -> dict[str, float]:
# ИСПОЛЬЗОВАТЬ: либо, мы могли бы написать совсем другую сигнатуру:
# def average(*args: Real, seq: NumSeq = None) -> dict[str, float]:
	"""Функция принимает на вход один аргумент: list, tuple или str, содержащий только целые или вещественные числа. Функция возвращает отсортированный словарь для среднего арифметического, геометрического, квадратичного и гармонического значения аргументов."""
	# ИСПРАВИТЬ: встроенная функция isinstance() больше подходит для таких проверок
	# ИСПРАВИТЬ: почему только первый аргумент проверяете? у вас ещё целый кортеж их
	if type(string) not in (str, list, tuple, int, float):
		return None

	if len(args) != 0:
		# ИСПРАВИТЬ: что если в string был передан контейнер, а дальше числа? вы получите список со вложенным контейнером под индексом 0 и числа далее
		# ИСПРАВИТЬ: если вам нужно просто преобразовать кортеж в список, то используйте функцию list()
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


# СДЕЛАТЬ: доработайте функцию из задачи 5 задания 08.22, и только затем займитесь функцией в этой задаче


# ИТОГ: не идеальный, но рабочий вариант — 4/5
