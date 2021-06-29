boys = []
girls = []
boys = input().split()
girls = input().split()
if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары!')
else:
    boys.sort()
    girls.sort()
    print('Идеальные пары:')
    for i in range(len(boys)):
        print(boys[i] ,' и ', girls[i])
