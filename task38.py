# Задача 38: Создать телефонный справочник возможностью добавления записей и 
# чтения. Пользователь также может ввести фамилию, тогда программа должны вывести
# на экран все записи с этой фамилий. 
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.

mode = int(input('Enter the mode: 1 - import, 2 - export: '))
if mode == 1:
    surname = input('Enter surname: ')
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    with open ('spravochnik.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    with open ('spravochnik.txt', 'a', encoding='utf-8') as file:   
        file.write(surname +'\n')
        file.write(name +'\n')
        file.write(phone +'\n')
        file.write('\n' * 1)

if mode == 2:
    surname = input('Enter surname: ')
    with open ('spravochnik.txt', 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        #print(text)
        text1 = list(filter(len, map(str.strip, text)))
        #print(text1)
        list1 = [[i, j, g] for i, j, g in zip(text1[0::3], text1[1::3],text1[2::3])]                                         
        #print(list1)
        for list2 in list1:
            for srn in list2:
                if srn == surname:
                    print(' '.join(list2))
else:
    print('Incorrect mode!')
    