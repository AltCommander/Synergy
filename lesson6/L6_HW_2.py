#Получаем натуральное число X
x = int(input("Введите натуральное число X: "))

#Производим вычисления
divisors_count = 1
current_factor = 2

while x > 1:
    power = 0
    while x % current_factor == 0:
        x //= current_factor
        power += 1
    
    if power > 0:
        divisors_count *= (power + 1)

    current_factor += 1

#Выводим результат
print(f"У числа X {divisors_count} натуральных делителей")