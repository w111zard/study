def get_index_of_smallest(array):
    smallest_value = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest_value:
            smallest_value = array[i]
            smallest_index = i

    return smallest_index


def selection_sort(array):
    sorted_array = []
    
    for i in range(len(array)):
        smallest_value_index = get_index_of_smallest(array)
        sorted_array.append(array.pop(smallest_value_index))

    return sorted_array


array = [5, 3, 10, 20, 9, 7, 8]
sorted_array = selection_sort(array)
print(*sorted_array)
