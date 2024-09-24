n = int(input())
x=0
for j in range(n):
    flag=True
    for s in range(4):
        if int(input())<4 and flag:
            x+=1
            flag=False
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", x)