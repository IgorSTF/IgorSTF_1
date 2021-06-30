phrase_1 = input()
phrase_2 = input()
if len(phrase_1) > len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
elif len(phrase_1) == len(phrase_2):
    print('Фразы одинаковой длины')
else:
    print('Фраза 2 длиннее фразы 1')
    