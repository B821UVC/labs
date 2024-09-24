'''В группе учится п студентов. Каждый сдал 4 экзамена. Подсчи-
тать число неуспевающих студентов и средний балл группы.'''
print("в однгой строке вводите одну оценку")
x=0
avg_score=0
n=0
while True:
    try:
        flag=True
        n+=1
        for s in range(4):
            num = int(input())
            avg_score+=int(num)
            if num<4 and flag:
                x+=1
                flag=False
    except:
        break
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", x)
print(f"Средний балл группы: {avg_score/(4*n)}")
