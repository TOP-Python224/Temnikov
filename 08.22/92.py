# ИСПРАВИТЬ: несоответствие аннотации возвращаемого типа и типа возвращаемого значения
def get_day_and_month(year: int, day_count: int) -> int:
    # ИСПРАВИТЬ: перепишите описание функции по аналогии с задачей 91 — можно без подробного описания параметров и возвращаемого значения, главное, первую строку документации
    """Функция принимает на вход год и порядковый номер дня, и возвращает дату."""
    d_in_m = [31, 28+is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(len(d_in_m)):
        if day_count <= d_in_m[i]:
            # ИСПОЛЬЗОВАТЬ: при подстановке в f-строку, также как и при передаче в функцию print(), преобразование в строку осуществляется автоматически для всех объектов любых типов
            return f"{day_count}-{i + 1}-{year}"
        day_count -= d_in_m[i]


# ИСПРАВИТЬ: преобразование в список не нужно
year, day_count = list(map(int, input('Год и день в году: ').split()))
# ОТВЕТИТЬ: зачем поменяли порядок вычисления условий скобками?
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# ИСПОЛЬЗОВАТЬ: сравнение с None осуществляется с помощью оператора is
if get_day_and_month(year, day_count) is None:
    # ИСПОЛЬЗОВАТЬ: здесь лучше выбросить исключение
    raise ValueError("введено неверное количество дней")
else:
    # ИСПРАВИТЬ: функция вызывается с одинаковыми аргументами два раза — при проверке условия и здесь — это избыточно
    print(f'Дата: {get_day_and_month(year, day_count)}\n')

expiration_date = int(input("Введите срок годности/гарантии: "))

# ИСПОЛЬЗОВАТЬ: а здесь почему приведение bool к int не используете?
if 0 < day_count <= 365 + is_leap:
    end_day = day_count + expiration_date
    # ИСПРАВИТЬ: и здесь можно использовать объект bool — перепишите по аналогии с показанным мной примером в условии
    if is_leap and end_day > 366:
        year += end_day // 366
        day_count = end_day - 366
    elif not is_leap and end_day > 365:
        year += end_day // 365
        day_count = end_day - 365
    print(f"Дата окончания годности/гарантии: {get_day_and_month(year, day_count)}")


# stdout:
# Год и день в году: 2020 366
# Дата: 31-12-2020
# Введите гарантийный срок: 280
# Дата окончания годности/гарантии - 6-10-2021

# Год и день в году: 2019 366
# Введено неверное количество дней!


# ИТОГ: критичного ничего нет, но много моментов, на которые необходимо обратить внимание — 4/5
