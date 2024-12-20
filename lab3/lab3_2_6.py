
'''Задан одномерный массив и число Р. Включить элемент, рав-
ный Р, после того элемента массива, который наиболее близок к сред-
нему значению его элементов.'''
arr = [0, 3, 99, 15, 16, 55, 44, -31, 50]
#arr2 = [0, 9, 9, 17.3, -16.3, -14, 73, 58]
P = float(input("Введите число которое необходимо включить в список:"))

delta = 10**21
need_ps = 0

avg = 0
for i in range(len(arr)):
    avg+=arr[i]
avg = avg/len(arr)


for ps,i in enumerate(arr):
    if (abs(avg-i)<delta):
        need_ps = ps
        delta = abs(avg-i)

arr = arr[:need_ps+1] +[P]+ arr[need_ps+1:] 
print("Среднее значение: ", avg)
print(arr)
