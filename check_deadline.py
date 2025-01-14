
from datetime import datetime

# определяем текущую дату
now = datetime.now().strftime("%d-%m-%Y")
print("Текущая дата:", now)
current_date = datetime.strptime(now, '%d-%m-%Y')

# блок определения дедлайна заметки
while True:
    try:
        deadline_str = input("Введите дату дедлайна (в формате дд-мм-гггг): ")

        # преобразования даты дедлайна в формат даты из формата строки
        deadline_date = datetime.strptime(deadline_str, '%d-%m-%Y')
        print(deadline_date)
        # производим сравнение дат - дедлайна и текущей
        time_difference = deadline_date - current_date
        day_difference = time_difference.days

        # определяем статус дедлайна
        if day_difference < 0:
            print(f"Внимание! Дедлайн истёк {abs(day_difference):02d} дней назад.")
        elif day_difference == 0:
            print("Дедлайн сегодня!")
        else :
            print(f"До дедлайна осталось {day_difference :02d} дней ")
        break

        # обработка неверного формата даты
    except ValueError:
        print("Ошибка! Пожалуйста, введите дату в правильном формате(дд-мм-гггг).")
        print("Пример: 25-12-2024")







