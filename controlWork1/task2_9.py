'''9. В соревнованиях по плаванию на 200 м участвуют n спортсмен-
но в. Вывести на печать лучший результат.'''
n = int(input("Введите число спортсменов: "))
print("Введите время спортсменов. Каждое число с новой строки")

def set_lst(n)->list:
    arr = []
    for i in range(n):
        arr.append(float(input()))
    return arr

def best_time(arr):
    print("Лучшее время :", min(arr))

best_time(set_lst(n))


#test 
test_arr = [189, 187, 200, 211, 185]  #return 185
best_time(test_arr)