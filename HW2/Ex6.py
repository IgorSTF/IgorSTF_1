
numbers = input().split()
numbers = [int(i) for i in numbers]
print(numbers)
i =0
while i < len(numbers)-1:
    j = i
    while j < len(numbers)-1:
        if numbers[i] == numbers[j+1]:
            del numbers[j+1]
        else:
            j+=1
    i += 1
print(numbers)