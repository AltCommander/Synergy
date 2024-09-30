#Получаем введенное слово
word = input("Enter word: ")

#Считаем гласные буквы в слове
if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
    print(True)
else:
    print(False)

#Определяем частоту гласных букв в слове
count_a = word.count('a')
count_e = word.count('e')
count_i = word.count('i')
count_o = word.count('o')
count_u = word.count('u')

#Выводим полученные данные

print("Count of 'a':", count_a)
print("Count of 'e':", count_e)
print("Count of 'i':", count_i)
print("Count of 'o':", count_o)
print("Count of 'u':", count_u)