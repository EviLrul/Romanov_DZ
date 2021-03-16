# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого):
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_jokes = []
number_of_jokes = 0


def get_jokes(number, uniqueness_option=0):
    """
    Функция составляет шутки из 3 списков, беря рандомно из каждого по одному слову.

    :param uniqueness_option: опция на уникальность используемых слов
    :param number: колличество шуток
    :return:
    """
    for i in range(number):
        if uniqueness_option == 0:
            list_jokes.append(choice(nouns) + " " + choice(adverbs) + " " + choice(adjectives))
        elif uniqueness_option == 1:
            nouns_index = nouns.index(choice(nouns))
            temp_text = nouns.pop(nouns_index)
            adverbs_index = adverbs.index((choice(adverbs)))
            temp_text = temp_text + " " + adverbs.pop(adverbs_index)
            adjectives_index = adjectives.index(choice(adjectives))
            temp_text = temp_text + " " + adjectives.pop(adjectives_index)
            list_jokes.append(temp_text)
            temp_text = ""


while True:
    try:
        number_of_jokes = int(input("Введите количество шуток от 1 до 5: "))
        uniqueness_option = int(input("Введите будут ли шутки формироваться с повторением слов - '0' или же "
                                      "слова будут уникальны - '1': "))
        if (0 < number_of_jokes < 6) and (-1 < uniqueness_option < 2):
            break
    except ValueError:
        print("Вы ввели не верное колличество шуток")

get_jokes(number_of_jokes, uniqueness_option)
print()
print(list_jokes)
