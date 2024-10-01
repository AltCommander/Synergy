#Получаем число N
n = int(input("Введите число N: "))

#Вводим N чисел
count = 0

for i in range(n):
    num = int(input("Введите целое число: "))
    if num == 0:
        count += 1

#Выводим результат
print("Количество нулей:", count)