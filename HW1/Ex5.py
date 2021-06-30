number = int(input())
s1 = number//100000 + number % 100000 // 10000 + number % 10000 // 1000
s2 = number % 1000 // 100+ number % 100 // 10 + number % 10
if s1 == s2:
    print('Счастливый билет')
else:
    print('Не счастливый билет')