#Вычисляем факториал числа
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

#Получаем число
n = int(input("Введите ваше число:\n"))

#Вычисляем факториал введенного числа
f_num = factorial(n)

#Вычисляем факториалы всех чисел от f_num до 1
f_list = []
for i in range(f_num, 0, -1):
    f_list.append(factorial(i))

#Выводим результат
print(f_list)