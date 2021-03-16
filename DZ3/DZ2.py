# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную
# работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

translation_response = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(translation_word):
    if translation_word.istitle():
        print(translation_response.get(translation_word.lower(), "None").title())
    else:
        print(translation_response.get(translation_word, "None"))


while True:
    translation_request = input("Введите числительную от 0 до 10 на английском языке для первода "
                                "её на русский (для выхода введите 00): ")
    if translation_request == "00":
        break
    num_translate(translation_request)
