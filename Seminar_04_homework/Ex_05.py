# Ex_5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

# Функция рандомного создания многочленов 
# и запись их в соответствующие файлы
def equation(x):
    degreeK = 2
    equation_temp = ""
    for i in range(degreeK, -1, -1):
        number = random.randint(1, 100)
        if number > 0:        
            if i > 1:        
                equation_temp += str(number) + "*x^" + str(i) + " + "
            elif i == 1:
                equation_temp += str(number) + "*x" + " + "
            else:          
                equation_temp += str(number) + " = 0"
    # print(f"Уравнение {x} степени {degreeK}: {equation_temp}")
    data = open (f'Ex_05_file_{x}.txt', 'w')
    data.writelines(equation_temp)
    data.close()

equation(1)
equation(2)

# Функция возврата строки уровнения из файла
def file_temp(x):
    path = f'Ex_05_file_{x}.txt'
    data = open(path, 'r')
    for line in data:
        return line
    data.close()

# Функция нахождения множителей уравнения
def sum_equet(y):
    list1 = y[:-4:].split(" + ")
    list2 = []
    for i in range(len(list1)):
        list1[i] = list1[i].split("*")
        list2.append(int(list1[i][0]))
    return list2

equet1 = file_temp(1)
print(f"Первое уравнение: {equet1}")
equet2 = file_temp(2)
print(f"Второе уравнение: {equet2}")

coefficients_1 = sum_equet(equet1)
coefficients_2 = sum_equet(equet2)

# Записываем уравнение с суммой множителей других уравнений
list3 = equet1.split(" + ")
for i in range(len(list3)):   
    list3[i] = list3[i].replace(str(coefficients_1[i]), str(coefficients_1[i] + coefficients_2[i]))
equet3 = " + ".join(list3)
print(f"Итоговое уравнение: {equet3}")

data = open (f'Ex_05_file_3.txt', 'w')
data.writelines(equet3)
data.close()