# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

in_put = int(input('Введите конечное число: '))
new_gen = (el for el in range(1, in_put+1, 2))

print(next(new_gen), type(new_gen))
print(next(new_gen), type(new_gen))
print(next(new_gen), type(new_gen))
for i in new_gen:
    print(i, type(i))

