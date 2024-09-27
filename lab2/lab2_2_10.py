'''В группе учится п студентов. Каждый получил на экзаменах по
4 оценки. Подсчитать число студентов, не имеющих «2» и «3»'''
#tests 
def count_2_3(lst:list, n:int)->int:
    indx=0
    result = 0
    for j in range(n):
        flag = True
        for s in range(4):
            if lst[indx]==2 or lst[indx]==3 and flag:
                result+=1
                flag = False
            indx+=1
    return result


#tests
n1 = 2
check1 = [3,3,3,3,5,5,5,5]

n2 = 1
check2 = [3,5,3,3]

n3 = 1
check3 = [5,5,5,5]

n4 = 1
check4 = [5,4,2,4]
print("Количество студентов у которых нет оценок 2 или 3 :", count_2_3(check1, n1))
print("Количество студентов у которых нет оценок 2 или 3 :", count_2_3(check2, n2))
print("Количество студентов у которых нет оценок 2 или 3 :", count_2_3(check3, n3))
print("Количество студентов у которых нет оценок 2 или 3 :", count_2_3(check4, n4))



n = int(input("Введите количество студентов:"))
print("Вводите по одной оценке в строке")
lst = [int(input()) for x in range(4*n)]
print("Количество студентов у которых нет оценок 2 или 3 :", count_2_3(lst, n))
