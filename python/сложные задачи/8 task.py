def determine_season(day, month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"

day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

season = determine_season(day, month)
print(f"Дата {day}.{month} попадает в сезон: {season}.")
