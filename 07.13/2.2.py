sum = 0

for num in range(100, 999):
    num1 = num / 100
    num2 = num % 10
    num3 = (num % 100) / 10
    if num1 == num2 or num2 == num3 or num1 == num3:
        sum += 1
        
print(sum)