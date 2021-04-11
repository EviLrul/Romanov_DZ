# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
# функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


from functools import wraps


def uslovie(_func):
    # print('Проверка')

    def decor(func):
        # print('Обёртка')

        @wraps(func)
        def wrapper(args):
            # print('Действия в обёртке')
            if _func(args):
                print(func(args))
            else:
                raise ValueError('Отрицательное значение')
            return func

        return wrapper

    return decor


@uslovie(lambda x: x > 0)
def calc_cube(i):
    # print('Функция корня')
    return i ** 3


in_put = calc_cube(5)
