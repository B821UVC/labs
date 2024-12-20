'''Включить заданный элемент P полсе последнего положительногоэлемента массива'''
import random
#lst = [random.randint(-10, 25) for x in range(20)]
P = int(input("Введите число которое необходимо включить в список: "))
def task(P, lst):
    lst_positive_indx = 0
    for i in range(len(lst)):
        if lst[i]>0:
            lst_positive_indx = i
    res = lst[:lst_positive_indx+1] +[P]+ lst[lst_positive_indx+1:] 
    print("Исходный список: ", lst)
    print("Результат: ", res)

for i in range(3):
    lst = [random.randint(-11, 5) for x in range(20)]
    print("Тест 1")
    task(P, lst)
    lst = [random.randint(-10, 25) for x in range(20)]
    print("Тест 2")
    task(P, lst)
    lst = [random.randint(-10, 20) for x in range(28)]
    print("Тест 3")
    task(P, lst)