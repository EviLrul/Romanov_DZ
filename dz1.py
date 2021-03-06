input_seconds = int(input("Введите количество секунд "))
minutes_output = input_seconds // 60
seconds_output = input_seconds % 60
hours_output = input_seconds // 3600
minutes_output = minutes_output % 60
days_output = hours_output // 24
hours_output = hours_output % 24
print(days_output, "день(дней/я)", hours_output, "час(ов/а)",  minutes_output, "минут(ы)", seconds_output, "секунд(ы)")
