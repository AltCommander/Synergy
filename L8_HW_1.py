#Получаем число N и вводим числа
n = int(input("Введите число N:"))
res = []
for i in range(n):
    res.append(int(input("Введите число:")))

#Выводим результат
res.reverse()
print(res)