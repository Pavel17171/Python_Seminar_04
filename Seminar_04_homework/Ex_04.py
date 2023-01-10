# Ex_4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.
#     Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

degreeK = int(input("Введите натуральную степень: "))
list1 = []
equation = ""

if degreeK > 0:
    for i in range(degreeK, -1, -1):
        number = random.randint(0, 100)
        if number > 0:        
            if i > 1:        
                list1.append(str(number) + "*x^" + str(i))                 
            elif i == 1:
                list1.append(str(number) + "*x")
            else:          
                list1.append(str(number))

    for i in range(len(list1)):
        if i < len(list1) - 1:
            equation += list1[i] + " + "
        else:
            equation += list1[i] + " = 0"
    if 'x' in equation:    
        print(f"Уравнение степени {degreeK}: {equation}")
        data = open ('Ex_04_file.txt', 'w')
        data.writelines(equation)
        data.close()
    else:
        print("Уравнение не содержит 'x'")
else:
    print("Введеное число не соответствует условию")