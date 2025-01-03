
username = input('Назовите себя: ')
title = input('Назовите вашу заметку: ')
header1 = input('Введите название 1 заголовка: ')
header2 = input('Введите название 2 заголовка: ')
header3 = input('Введите название 3 заголовка: ')
headlines = [header1, header2, header3]
content = input('Введите текст заметки: ')
created_date = input('Введите дату начала в формате дд-мм-гг ')
issue_date = input('Введите дату окончания в формате дд-мм-гг ')
note = [
    username,
    title,
    content,
    created_date,
    issue_date,
    headlines
]
print(note)


