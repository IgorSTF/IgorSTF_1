countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
print(len(countries_temperature))
for i in range(len(countries_temperature)):
    sum = 0
    for j in range(len(countries_temperature[i][1])):
        sum+=(countries_temperature[i][1][j]-32)/1.8
    print(countries_temperature[i][0], round(sum/len(countries_temperature[i][1]),1))