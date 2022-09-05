n = int(input(' > '))
arr = []
while n > 0:
    n, k = divmod(n, 10)
    if k not in (3, 6):
        arr.append(k)
x = 0
for i, v in enumerate(arr):
    x += v * 10**i
print(x)