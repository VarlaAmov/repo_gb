list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0

for x in list:
    if list[i] == '+5':
        list[i] = '"+05"'
    elif list[i].isdigit():
       list[i] = f'"{int(list[i]):02}"'
    print(list[i], end=' ')
    i += 1

