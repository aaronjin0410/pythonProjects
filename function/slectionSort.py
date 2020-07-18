def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[min_index], list[i] = list[i], list[min_index]
    print(list)


list = [1, 3, 2, 6, 4]
selectionSort(list)
