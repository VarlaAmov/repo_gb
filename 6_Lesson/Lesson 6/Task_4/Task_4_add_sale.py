from sys import argv

with open('bakery.csv', mode='a', encoding='utf-8') as f_add:

    if argv[1].isdigit():
        f_add.write(argv[1])
        f_add.write('\n')
    else:
        print('Не правильно заданный параметр')
