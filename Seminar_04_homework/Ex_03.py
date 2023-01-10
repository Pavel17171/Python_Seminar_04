#Ex_3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

# Рандомное зополнение списка
number = randint(1, 10)
list1 = []
for i in range(number):
    list1.append(randint(1, 5))
print(f"Исходный список: {list1}")

# Вывод неповторяющихся значений
list2 = []
for i in range(number):
    if list1.count(list1[i]) == 1:
        list2.append(list1[i])
#list2.sort()
print(f"Неповторяющиеся значения: {list2}")