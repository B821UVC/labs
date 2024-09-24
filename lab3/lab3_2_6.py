#arr = [float(x) for x in input().split()]
arr = [0, 3, 99, 15, 16, 55, 44, -31, 50]
arr2 = [0, 9, 9, 17.3, -16.3, -14, 73, 58]
P = float(input())

delta = 10**21
need_ps = 0
for ps,i in enumerate(arr):
    if (abs(P-i)<delta):
        need_ps = ps
        delta = abs(P-i)

arr = arr[:need_ps+1] +[P]+ arr[need_ps+1:] 
print(arr)
