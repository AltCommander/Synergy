# Получаем начальное и конечное значения диапазона
start = int(input("Введите начальное значение диапазона:\n"))
end = int(input("Введите конечное значение диапазона:\n"))

my_dict = dict()

#Получаем ключи словаря и заполняем его
if start <= end:
    for key in range(start, end + 1):
        my_dict[key] = key ** key
else:
    for key in range(start, end - 1, -1):
        my_dict[key] = key ** key

#Выводим результат
for key, value in my_dict.items():
    print(f"{key}: {value}")