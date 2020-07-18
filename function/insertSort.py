def insertSort(list):
    for i in range(len(list) - 1):
        for j in range(i, 0, -1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    print(list)


list = [4, 3, 2, 6, 1]
insertSort(list)
