print('Введите день')
day = int(input())
print('Введите месяц')
month = input().lower()
if (month == 'март' and day >=21 and day <= 31) or (month == 'апрель' and day >=1 and day <= 19):
    print('Ваш знак зодиака: Овен')
if (month == 'апрель' and day >=20 and day <= 30) or (month == 'май' and day >=1 and day <= 20):
    print('Ваш знак зодиака: Телец')
if (month == 'май' and day >=21 and day <= 31) or (month == 'июнь' and day >=1 and day <= 20):
    print('Ваш знак зодиака: Близнецы')
if (month == 'июнь' and day >= 21 and day <= 30) or (month == 'июль' and day >= 1 and day <= 22):
    print('Ваш знак зодиака: Рак')
if (month == 'июль' and day >= 23 and day <= 31) or (month == 'август' and day >= 1 and day <= 22):
    print('Ваш знак зодиака: Лев')
if (month == 'август' and day >= 23 and day <= 31) or (month == 'сентябрь' and day >= 1 and day <= 22):
    print('Ваш знак зодиака: Дева')
if (month == 'сентябрь' and day >= 23 and day <= 30) or (month == 'октябрь' and day >= 1 and day <= 22):
    print('Ваш знак зодиака: Весы')
if (month == 'октябрь' and day >= 23 and day <= 31) or (month == 'ноябрь' and day >= 1 and day <= 21):
    print('Ваш знак зодиака: Скорпион')
if (month == 'ноябрь' and day >= 22 and day <= 30) or (month == 'декабрь' and day >= 1 and day <= 21):
    print('Ваш знак зодиака: Стрелец')
if (month == 'декабрь' and day >= 22 and day <= 31) or (month == 'январь' and day >= 1 and day <= 19):
    print('Ваш знак зодиака: Козерог')
if (month == 'январь' and day >= 20 and day <= 31) or (month == 'февраль' and day >= 1 and day <= 18):
    print('Ваш знак зодиака: Водолей')
if (month == 'февраль' and day >= 19 and day <= 29) or (month == 'март' and day >= 1 and day <= 20):
    print('Ваш знак зодиака: Рыбы')