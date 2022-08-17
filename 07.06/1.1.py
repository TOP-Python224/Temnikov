name = input('Введите своё имя: ')
surname = input('Введите свою фамилию: ')
year_of_birth = input('Введите год рождения: ')
year_of_birth = int(year_of_birth)

age = 2022 - year_of_birth

print(f'{surname} {name}, {age}')