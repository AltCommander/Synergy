#Получаем натуральное число X
x = int(input("Введите натуральное число X: "))

#Производим вычисления
n2 = 0
n3 = 0
n5 = 0
n7 = 0
prime = False

while x != 1:
    if x % 2 == 0:
        x //= 2
        n2 += 1
    elif x % 3 == 0:
        x //= 3
        n3 += 1
    elif x % 5 == 0:
        x //= 5
        n5 += 1
    elif x % 7 == 0:
        x //= 7
        n7 += 1
    else:
        prime = True
        break

if not prime:
    result = (n2 + 1)*(n3 + 1)*(n5 + 1)*(n7 + 1)
else:
    result = 2

#Выводим результат
print("У числа X", result, "натуральных делителей")