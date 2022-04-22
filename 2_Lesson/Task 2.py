# 2. Задание
print('1.')
lst1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst1_final = []
i = 0

while i < len(lst1):
    if lst1[i].isdigit() or lst1[i][0] == '+' or lst1[i][0] == '-':
        lst1_final.append('"'), lst1_final.append(lst1[i]), lst1_final.append('" ')
    else:
        lst1_final.append(f'{lst1[i]} ')
    i += 1

for true_list in lst1_final:
    if true_list[0] == '+' or true_list[0] == '-':
        x, *f = list(true_list)
        y = ''.join(f)
        if y.find('.') == 1:
            true_list = f'{x}{y}'
        else:
            true_list = f'{x}{int(y):02}'
    elif true_list.isdigit():
        true_list = f'{int(true_list):02}'
    print(true_list, end='')


#__________________________________________________________________________________________________________________________________________________________________________
print('\n2.')

lst2 = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
lst2_final = []
i = 0

while i < len(lst2):
    if lst2[i].isdigit() or lst2[i][0] == '+' or lst2[i][0] == '-':
        lst2_final.append('"'), lst2_final.append(lst2[i]), lst2_final.append('" ')
    else:
        lst2_final.append(f'{lst2[i]} ')
    i += 1

for true_list in lst2_final:
    if true_list[0] == '+' or true_list[0] == '-':
        x, *f = list(true_list)
        y = ''.join(f)
        if y.find('.') == 1:
            true_list = f'{x}{y}'
        else:
            true_list = f'{x}{int(y):02}'
    elif true_list.isdigit():
        true_list = f'{int(true_list):02}'
    print(true_list, end='')

#__________________________________________________________________________________________________________________________________________________________________________
print('\n3.')

lst3 = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03', '05', 'секунд', 'температура', 'воздуха', 'была', '5', 'градусов Цельсия', 'темп','воды','+2.0','градусов','Цельсия' ,'-2', '11']
lst3_final = []
i = 0

while i < len(lst3):
    if lst3[i].isdigit() or lst3[i][0] == '+' or lst3[i][0] == '-':
        lst3_final.append('"'), lst3_final.append(lst3[i]), lst3_final.append('" ')
    else:
        lst3_final.append(f'{lst3[i]} ')
    i += 1

for true_list in lst3_final:
    if true_list[0] == '+' or true_list[0] == '-':
        x, *f = list(true_list)
        y = ''.join(f)
        if y.find('.') == 1:
            true_list = f'{x}{y}'
        else:
            true_list = f'{x}{int(y):02}'
    elif true_list.isdigit():
        true_list = f'{int(true_list):02}'
    print(true_list, end='')
