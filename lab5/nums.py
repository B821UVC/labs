from random import *

seed(2)
lst=[]
f=True
while f:
    k = randint(1, 29)
    if(k not in lst ):
        lst.append(k)
    if len(lst)==2:
        f = False
print(lst)
print(randint(1, 7))