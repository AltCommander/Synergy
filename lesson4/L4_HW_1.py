#Считываем длины сторон прямоугольника
print("Введите длины сторон прямоугольника через пробел:")
a, b = map(float, input().split())

#Выводим результаты
print("Площадь прямоугольника:", a * b)
print("Периметр прямоугольника:", 2 * (a + b))