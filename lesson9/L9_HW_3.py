#Получаем последовательность чисел
l1 = list(map(int, input("Введите последовательность чисел через пробел:\n").split()))

#Проверяем, встречалось ли число раньше
s1 = set()
for i in l1:
    if i in s1:
        print(f"{i}: YES")
    else:
        s1.add(i)
        print(f"{i}: NO")