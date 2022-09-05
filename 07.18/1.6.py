n = 0

for num in range (1, 999999 + 1):
    list_num = []
    while num:
        list_num.append(num % 10)
        num //= 10
    half = len(list_num) // 2
    summ = sum(list_num[:half])
    summ1 = sum(list_num[half:])
    if summ == summ1:
        n += 1

print(n)