from datetime import datetime

def is_valid_date(date_string):
    try:
        date = datetime.strptime(date_string, "%d.%m.%Y")
        print(f"Дата {date_string} корректна.")
    except ValueError:
        print(f"Дата {date_string} некорректна.")

# Пример использования
date_string = input("Введите дату в формате 'дд.мм.гггг': ")
is_valid_date(date_string)
