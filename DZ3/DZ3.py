# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?
list_of_employees = ['Вася', 'Петя', 'Катя', 'Коля']
final_dictionary = {}


def thesaurus(name):
    for i in range(len(name)):
        name_letter = name[i][0:1]
        if final_dictionary.get(name_letter) is None:
            final_dictionary.setdefault(name_letter, [name[i]])
        else:
            list_temp = final_dictionary.get(name_letter)
            list_temp.append(name[i])
            final_dictionary[name_letter] = list_temp
    return final_dictionary


print(thesaurus(list_of_employees))

temp_list = list(final_dictionary.keys())       # сортировка по ключам
temp_list.sort()
for n in temp_list:
    print(n, ':', final_dictionary[n])
