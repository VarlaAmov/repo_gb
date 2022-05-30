with open("nginx_logs.txt", mode='rt', encoding='utf-8') as file:
    # Возможное решение
    lst_final = []
    for i in file:
        i = i.replace('"', ' ').split()
        _ = i[0],i[5],i[6]
        lst_final.append(_)
    print(*lst_final, sep='\n')
