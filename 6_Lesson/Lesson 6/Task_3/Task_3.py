with open('task_3_users.csv', mode='rt', encoding='utf-8') as f_users:
    full_names = []
    for i in f_users:
        i = i.strip().split(',')
        i = i[0][0] + i[1][0] + i[2][0]
        full_names.append(i)

with open('task_3_hobby.csv', mode='rt', encoding='utf-8') as f_hobby:
    hobby = []
    for i in f_hobby:
        i = i.replace(',', ';').strip()
        hobby.append(i)

dct_users_and_hobby = {}
for i in range(len(full_names)):
    if i < len(hobby):
        dct_users_and_hobby[full_names[i]] = hobby[i]
    else:
        dct_users_and_hobby[full_names[i]] = None

if len(hobby) > len(full_names):
    print(dct_users_and_hobby)
    exit(1)
else:
    print(dct_users_and_hobby)

with open('task_3_rezult.txt', mode='wt', encoding='utf-8') as f_rezult:
    f_rezult.write(str(dct_users_and_hobby))

