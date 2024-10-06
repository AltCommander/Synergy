import collections

#Создаём питомца
def create():
    if len(pets) == 0:
        last = 0
    else:
        last = collections.deque(pets, maxlen=1)[0] + 1

    name = input("Имя вашего питомца:\n")
    pet_type = input("Вид вашего питомца:\n")
    age = int(input("Возраст вашего питомца:\n"))
    owner = input("Имя хозяина:\n")

    pets[last] = {
        name:{
    "Вид питомца": pet_type,
    "Возраст питомца": age,
    "Имя владельца": owner
        }
    }

#Выводим информацию о питомце
def read():
    ID = int(input("Введите ID вашего питомца:\n"))
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0]
        pet_info = pet[name]
        print(f"Это {pet_info['Вид питомца']} по кличке \"{name}\". "
        f"Возраст питомца: {pet_info['Возраст питомца']} {get_suffix(pet_info['Возраст питомца'])}. "
        f"Имя владельца: {pet_info['Имя владельца']}")
    else:
        print("Питомец не найден.")

#Изменяем информацию о питомце
def update():
    ID = int(input("Введите ID питомца для изменения:\n"))
    pet = get_pet(ID)
    if pet:
        name = list(pet.keys())[0]
        pet_info = pet[name]
        pet_info['Вид питомца'] = input("Введите новый вид питомца:\n")
        pet_info['Возраст питомца'] = int(input("Введите новый возраст питомца:\n"))
        pet_info['Имя владельца'] = input("Введите новое имя владельца:\n")
        print(f"Информация о питомце с ID {ID} изменена.")
    else:
        print("Питомец не найден.")
    return

#Удаляем питомца
def delete():
    ID = int(input("Введите ID питомца для удаления:\n"))
    pet = get_pet(ID)
    if pet:
        pets.pop(ID)
        print(f"Питомец с ID {ID} удален.")
    else:
        print("Питомец не найден.")

#Получаем информацию о питомце по ID
def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

#Выбираем суффикс по году
def get_suffix(age):
    if 11 <= age <= 20 or age % 10 in (5, 6, 7, 8, 9, 0):
        postf = "лет"
    elif age % 10 == 1:
        postf = "год"
    elif age % 10 in (2, 3, 4):
        postf = "года"
    return postf

#Список питомцев
def pets_list():
    if not pets:
        print("Питомцев в базе нет.")
    else:
        for ID, pet in pets.items():
            name = list(pet.keys())[0]
            pet_info = pet[name]
            print(f"ID: {ID}, Это {pet_info['Вид питомца']} по кличке \"{name}\". "
                  f"Возраст: {pet_info['Возраст питомца']} {get_suffix(pet_info['Возраст питомца'])}. "
                  f"Имя владельца: {pet_info['Имя владельца']}")
            print("################################")

#Создаём необходимый нам словарь и получаем команды пользователя
pets = dict()

command = ""
while command != "stop":
    command = input("Введите комманду:\n")
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "pets_list":
        pets_list()
    elif command == "delete":
        delete()
    elif command == "stop":
        break
    else:
        print("Неизвестная команда. Пожалуйста, введите одну из команд: create, read, update, delete, pets_list, stop.")
