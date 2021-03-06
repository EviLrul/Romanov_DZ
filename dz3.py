percent = int(input("Введите процент: "))
while (percent < 1) or (20 < percent):
    if (percent < 1) or (20 < percent):
        print("Вы ввели не правильный диапазон. Ввод должен быть от 1 до 20")
        percent = int(input("Введите процент: "))
remainder = percent % 10
if 4 < percent < 21:
    print("Вы ввели", percent, "процентов")
elif remainder == 1:
    print("Вы ввели", percent, "процент")
elif 1 < remainder < 5:
    print("Вы ввели", percent, "процента")
