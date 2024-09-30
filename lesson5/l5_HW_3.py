#Получаем минимальную сумму
i_min = int(input("Enter minimum sum: "))

#Получаем деньги инвесторов
mike = int(input("Enter Mike's money: "))
ivan = int(input("Enter Ivan's money: "))

#Делаем расчеты
if mike >= i_min and ivan >= i_min:
    print(2)
elif mike >= i_min:
    print("Mike")
elif ivan >= i_min:
    print("Ivan")
elif mike + ivan >= i_min:
    print(1)
else:
    print(0)