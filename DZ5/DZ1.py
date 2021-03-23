# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:

def new_gener(_in_put):
    new_gen = (el for el in range(1, in_put + 1, 2))
    for i in new_gen:
        yield i


in_put = int(input('Введите конечное число: '))
x = new_gener(in_put)
print(*x, type(x))

