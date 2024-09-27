'''В группе учится п студентов. Каждый сдал 4 экзамена. Подсчи-
тать число неуспевающих студентов и средний балл группы'''

def avg_score_and_counts(n:int, lst:list): 
    x=0
    avg_score=0
    indx = 0
    for j in range(n):
        flag=True
        for s in range(4):
            avg_score+=lst[indx]
            if lst[indx]<4 and flag:
                x+=1
                flag=False
            indx+=1
    return [avg_score/(4*n), x]

n1 = 2
check1 = [3,3,3,3,5,5,5,5]
n2 = 1
check2 = [3,5,3,3]
n3 = 1
check3 = [5,5,5,5]
n4 = 1
check4 = [5,4,2,4]
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", avg_score_and_counts(n1, check1)[1])
print(f"Средний балл группы: {avg_score_and_counts(n1, check1)[0]}")
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", avg_score_and_counts(n2, check2)[1])
print(f"Средний балл группы: {avg_score_and_counts(n2, check2)[0]}")
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", avg_score_and_counts(n3, check3)[1])
print(f"Средний балл группы: {avg_score_and_counts(n3, check3)[0]}")
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", avg_score_and_counts(n4, check4)[1])
print(f"Средний балл группы: {avg_score_and_counts(n4, check4)[0]}")



n = int(input())
lst = [int(input()) for x in range(4*n)]
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", avg_score_and_counts(n, lst)[1])
print(f"Средний балл группы: {avg_score_and_counts(n, lst)[0]}")
