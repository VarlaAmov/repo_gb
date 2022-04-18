#Commit
#1 Задание
sec = int(input('Введите нужное кол-во секунд: '))

day = sec // 86400
hour = sec // 3600
min = sec // 60

if sec < 60:
    print(sec, "сек")
elif sec >= 60 and sec < 3600:
    sec %= 60
    print(f'{min} мин {sec} сек')
elif sec >= 3600 and sec < 86400:
    sec %= 60
    min %= 60
    print(f'{hour} час {min} мин {sec} сек')
elif sec >= 86400 and sec < 2678400:
    sec %= 60
    min %= 60
    hour %= 24
    print(f'{day} дн {hour} час {min} мин {sec} сек')
else:
    print('Error!!!\nПревышено допустимое кол-во секунд!')
