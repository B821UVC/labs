'''В массивах А размером 9 и В размером 7 заменить максималь-
ные элементы на среднее арифметическое значение элементов, рас-
положенных после максимального, в том массиве, для которого мак-
симальный элемент расположен дальше от конца массива. Поиск
максимального элемента осуществить в методе.'''

arrA=[2, 125, 14, 19, 78, 34, 9]
arrB=[17, 66, 78, 12, 56, 66, 89, 6778, 1]


def find_max_and_index(arr):
    max_value = arr[0]
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
    return max_value, max_index


def replace_with_average(arr):
    max_value, max_index = find_max_and_index(arr)
    if max_index < len(arr) - 1:
        average = sum(arr[max_index + 1:]) / (len(arr) - max_index - 1)
        arr[max_index] = average
    return arr


def process_arrays(array_a, array_b):
    index_a = len(array_a) - 1 - find_max_and_index(array_a)[1]
    index_b = len(array_b) - 1 - find_max_and_index(array_b)[1]
    
    if index_a > index_b:
        return replace_with_average(array_a), array_b
    else:
        return array_a, replace_with_average(array_b)
    

a_, b_ = process_arrays(arrA, arrB)
print("A: ", a_)
print("B: ", b_)