'''такое же условие как 2_10'''

x=0
while True:
    try:
        flag=True
        for s in range(4):

            
            if int(int(input()))<4 and flag:
                x+=1
                flag=False
    except:
        break
print("Количество студентов у которых хотя бы одна оценка 2 или 3 :", x)
