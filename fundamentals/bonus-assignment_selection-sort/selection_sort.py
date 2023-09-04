def selection_sort(list):
    for i in range(0, len(list)):
        min_value = list[i]
        for j in range (i+1, len(list)):
            min_index = i
            if list[j] < min_value:
                min_value = list[j]
                min_index = j
            print(min_value, min_index)
            list[i], list[j] = list[j], list[i]
            print("pass complete")

    return list

test = [5, 3, 4, 2, 6, 8, 7, 1]
print(selection_sort(test))