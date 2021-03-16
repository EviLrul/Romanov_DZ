# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"#
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
translation_response = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(translation_word):
    print(translation_response.get(translation_word, "None").title())


while True:
    translation_request = input("Введите числительную от 0 до 10 на английском языке для первода "
                                "её на русский (для выхода введите 00): ")
    if translation_request == "00":
        break
    num_translate(translation_request.lower())
