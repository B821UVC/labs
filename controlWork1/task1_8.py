'''7. Начав тренировки, спортсмен в первый день пробежал 10 км.
Каждый следующий день он увеличивал дневную норму на 10 % от
нормы предыдущего дня. Определить:
8. а) какой суммарный путь пробежит спортсмен за 7 дней;
б) через сколько дней спортсмен пробежит суммарный путь
100 км;
в) через сколько дней спортсмен будет пробегать в день больше
20 км?'''
#a
first_r = 10
all=10
for i in range(6):
    first_r  = first_r*1.1
    all+= first_r
print("Суммарный путь за 7 дней: ",all)

#б
all = 10
first_r = 10
day = 1
while all<100:
    all+=first_r*1.1
    day+=1
    first_r = first_r*1.1
print("День, когда спортсмен суммарно пробежит более 100км: ",day)
#в
first_r = 10
day = 1
while first_r<20:
    day+=1
    first_r = first_r*1.1
print("День, когда спортсмен пробежит больше 20км: ",day)