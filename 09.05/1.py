from random import randrange as rr


list1 = [rr(0, 50, 5) for _ in range(5)]
list2 = [rr(0, 50, 5) for _ in range(5)]

print(list1, list2, sep='\n', end='\n\n')

for num in set(list1) & set(list2):
	for item in (list1, list2):
		for i in range(item.count(num)):
			item.remove(num)
print(list1, list2, sep='\n')


# stdout 1:
# [10, 20, 30, 15, 20]
# [35, 0, 20, 0, 40]

# [10, 30, 15]
# [35, 0, 0, 40]

# stdout 2:
# [45, 25, 0, 45, 5]
# [40, 40, 25, 25, 40]

# [45, 0, 45, 5]
# [40, 40, 40]


# ИТОГ: отлично — 4/4
