# Задание 1
# Найти Максимальный элемент в списке из 5 элементов. (Не используя встроенные функции max())
# *Пример*
# Ввод: 3 -6 10 23 -14
# Ответ: 23

# list = [3 ,- 6, 10, 23, - 184]
# size = len(list)
# i = 0
# max = list[0]
# while i < size:
#     if list[i] > max:
#         max = list[i]
#         i += 1
#     else:
#         i += 1
# print(max)




char = input('Введите символ: ')
string1 = input('Введите строку: ')
count = 0

for elem in string1:
    if elem == char:
        count +=1
print(count)