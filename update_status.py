
status_tuple = ( '1', 'выполнено', '2', 'в процессе', '3', 'отложено' )
status = status_tuple[3]
print('Текущий статус заметки - ', status)

while True :                                     # цикл выбора статуса заметки и проверки правильности ввода данных

    a = input("Обновите статус вашей заметки  или в виде числа, где"
                       " 1 - выполнено, 2 - в процессе, 3 - отложено, \n или в в виде"
                       " текста: 'выполнено', 'в процессе', 'отложено':  ")
    a = ' '.join(a.split())                      # удаление ошибочно введенных пробелов

    if a == status_tuple[0] or a == status_tuple[1] :              # статус - выполнено
        status = status_tuple[1]
        print('текущий статус заметки обновлен на - ', status)
        break

    elif a == status_tuple[2] or a == status_tuple[3] :            # статус - в процессе
        status = status_tuple[3]
        print('текущий статус заметки обновлен на - ', status)
        break

    elif a == status_tuple[4] or a == status_tuple[5] :            # статус - отложено
        status = status_tuple[5]
        print('текущий статус заметки обновлен на - ', status)
        break

    else :
        print('вы неправильно ввели данные, попробуйте снова  ')

update_status = {'Текущий статус заметки: ' : status}




