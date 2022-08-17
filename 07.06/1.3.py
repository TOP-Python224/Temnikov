time = input()
time = int(time)

hours = time // 60
minute = time % 60

print(f'{time} мин - это {hours} час {minute} мин')