# Печатаем элементы списка от первого до последнего через рекурсию
def forward_count(l, f_it):
    if f_it >= len(l):
        print("Конец списка")
    else:
        print(l[f_it], end=' ')
        forward_count(l, f_it + 1)

#Задаём список и вызываем функцию обратной печати
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
forward_count(my_list, 0)