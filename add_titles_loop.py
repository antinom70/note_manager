headlines = []

while True:  # цикл добавления новых заголовков в список
    header = input('Введите название заголовка (или оставьте пустым для завершения): ')
    if header == '': break

    header = ' '.join(header.split())  # удаление ошибочно введенных пробелов
    headlines.append(header)

    a = headlines.count(header)  # проверка заголовков на повторяемость
    if a > 1:
        (headlines.pop(),
         print('Этот заголовок уже существует'))

print('Заголовки заметки: ')
for header in headlines:         # печать построчно заголовков заметки
    print('-', header)
