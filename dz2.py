i = 0
list_cubes = []
while i < 1000:                                    # создаем список от 0 до 1000
    remainder = i % 2                              # вычисляем в нем каждый не чётный элемент
    if remainder == 1:
        list_cubes.append(i**3)                    # формируем список с нечётным элементом в кубе
    i = i + 1
print("Список с кол-вом элементов", len(list_cubes), "выглядит следующим", list_cubes)

i = 0
number_items_found = 0
sum_list_items = 0
while i < len(list_cubes):                         # начинаем проверять каждый элемент списка
    n = list_cubes[i]
    sum_element_digits = 0
    while n > 0:                                   # суммируем цифры элемента списка
        end_digit = n % 10
        sum_element_digits = sum_element_digits + end_digit
        n = n // 10
    if sum_element_digits % 7 == 0:                # проверяем делится ли сумма цифр элемента на 7 если да то выводим
        number_items_found = number_items_found + 1
        # print("Номер элемента списка", i, "со значение", list_cubes[i], "сумма этого элемента равна", sum_element_digits, "и эта сумма делится на 7 без остатка")
        sum_list_items = sum_list_items + list_cubes[i]      # собираем сумму элементов, сумма цифр которые делятся на 7
    i = i + 1
print("Таких элементов", number_items_found)
print("Сумма элементов списка, сумма которых делится на 7 без остатка равна", sum_list_items)
print()

i = 0
while i < len(list_cubes):                         # увеличиваем все элементы списка на 17
    list_cubes[i] = list_cubes[i] + 17
    i = i + 1
print("Новый писок(+17) с кол-вом элементов", len(list_cubes), "выглядит следующим", list_cubes)

sum_list_items = 0
sum_element_digits = 0
i = 0
number_items_found = 0
while i < len(list_cubes):                         # начинаем проверять каждый элемент списка
    n = list_cubes[i]
    sum_element_digits = 0
    while n > 0:                                   # суммируем цифры элемента списка
        end_digit = n % 10
        sum_element_digits = sum_element_digits + end_digit
        n = n // 10
    if sum_element_digits % 7 == 0:                # проверяем делится ли сумма цифр элемента на 7 если да то выводим
        number_items_found = number_items_found + 1
        # print("Номер элемента списка", i, "со значение", list_cubes[i], "сумма этого элемента равна", sum_element_digits, "и эта сумма делится на 7 без остатка")
        sum_list_items = sum_list_items + list_cubes[i]      # собираем сумму элементов, сумма цифр которые делятся на 7
    i = i + 1
print("Таких элементов", number_items_found)
print("Сумма элементов списка, сумма которых делится на 7 без остатка равна", sum_list_items)
