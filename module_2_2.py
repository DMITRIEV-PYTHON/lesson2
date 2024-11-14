number_1 = input ("Введите число: ")
number_2 = input ("Введите число: ")
number_3 = input ("Введите число: ")
print(number_1)
print(number_2)
print(number_3)
if number_1 == number_2 and number_2 == number_3 and number_1 == number_3 :
    print(3, "одинаковых числа")
elif number_1 == number_2 or number_2 == number_3 or number_1 == number_3 :
    print(2, "два одинаковых числа")
else :
    print(0, "нет одинаковых чисел")
