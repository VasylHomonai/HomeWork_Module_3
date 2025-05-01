print('Перше завдання:')

from datetime import datetime

def get_days_from_today(date: str):
    try:
        # Перетворення рядка в дату
        date = datetime.strptime(date, "%Y-%m-%d").date()
        # Знаходження різниці між датами
        diff_days = (datetime.today().date() - date).days
    except ValueError as v:
        return f'Формат дати в рядку не відповідає формату в шаблоні РРРР-ММ-ДД: {v}'
    except TypeError as t:
        return f'У ф-цію передано не рядок: {t}'
    except Exception as e:
        return f'Виникла помилка: {e}'

    return diff_days

# Приклад для правильної дати, яка є ранішою за поточну
print(f"Різниця між датами: {get_days_from_today('2024-10-09')} днів")
# Приклад для правильної дати, яка є пізнішою за поточну
print(f"Різниця між датами: {get_days_from_today('2025-10-09')} днів")

# Приклад для винятку формату дати
print("Різниця між датами:", get_days_from_today('20-10-2009'))
# Приклад для винятку передачі не рядка
print("Різниця між датами:", get_days_from_today(20250101))

print('*' * 100, end='\n\n')


print('Друге завдання:')

import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    # Створення списку для набору випадкових чисел
    numbers_ticket = []             

    try:
        # Робляться провірки за заданими умовами задачі
        if (min >= 1) and (max <= 1_000) and (max+1 - min >= quantity): 
            # Заповнюємо список унікальними випадковими числами, які будуть відсортованими
            numbers_ticket = list(sorted(random.sample(range(min, max+1), quantity)))
    except Exception as e:
        return f'У ф-цію передано некоректні дані: {e}'

    return numbers_ticket

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers_2 = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers_2)

# Провірки на не валідність даних
print("Ваші лотерейні числа:", get_numbers_ticket(0, 36, 5))            # Пустий список
print("Ваші лотерейні числа:", get_numbers_ticket(1, 1001, 5))          # Пустий список
print("Ваші лотерейні числа:", get_numbers_ticket(30, 20, 5))           # Пустий список
print("Ваші лотерейні числа:", get_numbers_ticket(1, 10, 11))           # Пустий список

# Приклад для винятку передачі
print("Ваші лотерейні числа:", get_numbers_ticket('one', 'ten', 'four')) 

print('*' * 100, end='\n\n')


print('Третє завдання:')

import re

def normalize_phone(phone_number: str)-> str:
    # Провірка даних на тип str
    if not isinstance(phone_number, str):
        return 'Неправильний тип даних'

    # Провірка чи взагалі є хочаб одна цифра в рядку
    if not re.search(r'\d', phone_number):
        return 'Рядок немає жодної цифри'
    
    # Очищаємо рядок, залишаючи лише цифри
    digits  = re.sub(r'\D', '', phone_number)

    if re.match(r'^380', digits) and len(digits) == 12:
        # Якщо номер починається з "380" і має 12 цифр
        return re.sub(r'^(380)', r'+380', digits)
    elif re.match(r'^80', digits) and len(digits) == 11:
        # Якщо номер починається з "80" і має 11 цифр
        return re.sub(r'^(80)', r'+380', digits)
    elif re.match(r'^0', digits) and len(digits) == 10:
        # Якщо номер починається з "0" і має 10 цифр
        return re.sub(r'^(0)', r'+380', digits)
    else:
        return f"Неправильний формат номера. Номер: {digits}"


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050-11-22-22",
    "38050 111 22 11   ",
    "one two four ten nine zero",
    500000000
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)