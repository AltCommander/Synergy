#Получаем число N и вводим числа
n = int(input("Введите число N:"))
print(f"Введите {n} чисел через пробел:")
res = list(map(int, input().split()))

#Проверяем количество введённых чисел и выводим результат
if len(res) == n:
    res.insert(0, res[len(res)-1])
    res.pop()
    print("Изменённый массив:", res)
else:
    print("Ошибка! Введено неверное количество чисел.")