list = [1, 3, 2, 6, 4]

for i in range(len(list)):
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)
