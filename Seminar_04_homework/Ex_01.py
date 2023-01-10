#Ex_1. Вычислить число c заданной точностью d (10^(-1) ≤ d ≤ 10^(-10))
#     Пример:
# при d = 0.001, π = 3.141

import random
numInput = int(input("Введите количество знаков после запятой: "))
number = random.random() + random.randint(0, 100)
print(f"Исходное число: {number}")
numberRound = round(number, numInput)
print(f"Результат округления: {numberRound}")