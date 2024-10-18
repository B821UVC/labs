'''12. Первый отрицательный элемент массива заменить суммой эле-
ментов, расположенных после максимального.'''

print("Ведите список целых чисел, в котором есть хотя бы один отрицательный элемент, через пробел в одну строку")
arr = list(map(int, input().split()))

def change(arr):
    mx_val = -10**20
    mx_ind = -1
    first_otr = -1
    for i in range(len(arr)):
        if arr[i]<0 and first_otr==-1:
            first_otr = i
        if arr[i]>mx_val:
            mx_ind = i
            mx_val= arr[i]
    if mx_ind!=len(arr)-1:
        arr[first_otr] = sum(arr[mx_ind+1:])
        return arr
    else:
        return arr
    


#test
arr1 = [1, 5, -10, 4, 200, 30]
arr2 = [1,4,9,-10, 15, 20, -5, 10] 
def check(arr_test1, arr_test2):
    if arr_test1 == [1, 5, 30, 4, 200, 30]:
        print("первый тест верный")
    if arr_test2 == [1, 4, 9, 5, 15, 20, -5, 10]:
        print("второй тест верный")
check(change(arr1), change(arr2))

print(change(arr))


