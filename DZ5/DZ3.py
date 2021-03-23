# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести
# последние кортежи в виде: (<tutor>, None), например:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Матрона', 'Клава', 'Фёкла', 'Клавдий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def test(_tutors, _klasses):
    if len(klasses) < len(tutors):
        for q in range(len(_klasses)):
            yield _tutors[q], _klasses[q]
        for q in range(len(_klasses), len(_tutors)):
            yield _tutors[q], None
    else:
        for q in range(len(_tutors)):
            yield _tutors[q], _klasses[q]


print(tuple(test(tutors, klasses)))
