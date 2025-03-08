#1st
pw = input()
if pw == 'пароль':
    print('Проходи!')
else:
    print('Доступ запрещен!')

#2nd
first_radio = ['Генрих', 'Герц']
print('Какие два слова передал первой радиограммой Александр Попов?')
first_part = input('Первое слово: ')
second_part = input('Второе слово: ')
if first_radio[0] == first_part and first_radio[1] == second_part:
    print('Верно')
else:
    print('Неверно')

print('Как зовут главного персонажа Романов Яна Флеминга о вымышленном секретной разведывательной службы '
      'Великобритании')
name = input('Имя персонажа: ')
if name == 'Джеймс Бонд':
    print('Верно')
else:
    print('Неверно')

#4st
question = input('Вы поедете на бал? ')
if question.lower() != 'нет' and question.lower() != 'да':
    print('Верно')
else:
    print('Неверно')

#5st
N = int(input())
K = int(input())
if N>K:
    print(K)
elif K>N:
    print(N)
else:
    print(K)

#6th
table = list(map(int, input().split(sep=':')))
if table[0] > table[1]:
    print(1)
elif table[0] < table[1]:
    print(2)
else:
    print(0)

#7th
highlits = list(map(int, input().split()))
m = highlits[0]
for i in highlits:
    if i > m:
        m = i
print(m)

#8th
name = input('Здравствуйте! Как Вас зовут? ')
print(f'Очень приятно, {name.title()}! Меня зовут Марк')
age = int(input('Сколько Вам лет? '))
if age > 81:
    print(f'Да, {name.title()}, Вы старше меня на {age-81} лет')
else:
    print(f'Да, {name.title()}, я старше Вас на {81 - age} лет')
prog = input('Вам нравится программировать? ')
if prog.lower() == 'нет':
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня')
elif prog.lower() == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество интересных и хороших программ')

#9th
dog = input('Собака короткошерстной породы? ')
if dog == 'да':
    dog = input('Рост собаки менее 50 см? ')
    if dog == 'да':
        dog = input('У собаки которкий хвост? ')
        if dog == 'да':
            print('английский бульдог')
        elif dog == 'нет':
            dog = input('У собаки длинные уши? ')
            if dog == 'да':
                print('гончая')
            elif dog == 'нет':
                dog = input('У собаки короткое тело? ')
                if dog == 'да':
                    print('мопс')
                elif dog == 'нет':
                    print('чихуахуа')
    elif dog == 'нет':
        dog = input('Собака весит более 50 кг? ')
        if dog == 'да':
            print('датский дог')
        elif dog == 'нет':
            print('фоксхаунд')
elif dog == 'нет':
    dog = input('Рост собаки менее 50 см? ')
    if dog == 'да':
        dog = input('У собаки доброжедательный характер? ')
        if dog == 'да':
            print('кокер-спаниэль')
        elif dog == 'нет':
            print('ирландский сеттер')
    elif dog == 'нет':
        dog = input('У собаки рост менее 70 см? ')
        if dog == 'да':
            dog = input('У собаки длинные уши? ')
            if dog == 'да':
                print('большой вандейский грифон')
            elif dog == 'нет':
                print('колли')
        elif dog == 'нет':
            dog = input('Окрас рыжиц с белыми отметинами? ')
            if dog == 'да':
                print('сенбернар')
            elif dog == 'нет':
                dog = input('Белоснежный окрас? ')
                if dog == 'да':
                    print('ирландский волкодав')
                elif dog == 'нет':
                    print('ньюфаундлед')

#10th
machine = int(input())
if machine%2!=1:
    print('да')
else:
    print('нет')
