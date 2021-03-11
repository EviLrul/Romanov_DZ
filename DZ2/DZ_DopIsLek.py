# test_list = ['Hello', 42.00000014, True, [1, 2, 3], 1, 2, 'Basil']
# Доп задача -> убрать [1,2,3] и заменить на элементы большого списка 1, 2, 3 в том же месте
# Подсказка: index, insert, remove (опционально)

test_list = ['Hello', 42.00000014, True, [1, 2, 3], 1, 2, 'Basil', 45.0005, 'Hi all', ['one', 'two', 'three'], 84, '56']
el = 0
print("Старый список", test_list)
while el < len(test_list):
    if type(test_list[el]) == list:
        temp_list = test_list[el]
        for i in range(len(temp_list)):
            test_list.insert(test_list.index(test_list[el]), temp_list[i])
            el = el + 1
        test_list.pop(el)
    el = el + 1
print("Новый список", test_list)
