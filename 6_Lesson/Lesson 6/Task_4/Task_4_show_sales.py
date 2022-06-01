from sys import argv

with open('bakery.csv', mode='rt', encoding='utf-8') as f_read:
    read = f_read.read().strip().split('\n')

    for i in read:
        if len(argv) - 1 == 1:
            if argv[1].isdigit():
                print('\n'.join(read[int(argv[1]) - 1::]))
                break
            else:
                print('Не правильно заданный параметр')
                break
        elif len(argv) - 1 == 2:
            if argv[2].isdigit() and int(argv[2]) > int(argv[1]):
                print('\n'.join(read[int(argv[1]) - 1:int(argv[2])]))
                break
            else:
                print('Не правильно заданный параметр')
                break
        else:
            print(i)
