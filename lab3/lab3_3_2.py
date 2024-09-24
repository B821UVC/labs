'''В одномерном массиве увеличить максимальные элементы на
их порядковые номера (1-й максимальный - на 1; 2-й - на 2; 3-й - на
3 и т.д.).'''

arr = [10, 15, 44, 35]
max_elem = max(arr)
min_elem = min(arr)
negative_in_arr = False
if min_elem<0:
    struct = [[]for x in range(max_elem+1)]
    struct_negative = [[] for x in range(min_elem+1)]
    negative_in_arr = True
else:
    struct = [[]for x in range(max_elem+1)]

if negative_in_arr:
    for ps,num in enumerate(arr):
        if num>=0:
            struct[num].append(ps)
        else:
            struct_negative[-num].append(ps)
else:
    for ps,num in enumerate(arr):
        struct[num].append(ps)

add_var=0
if negative_in_arr:
    for rng in range(len(struct)-1, -1, -1):
        lst = struct[rng]
        if lst!=[0]:
            for i in range(len(lst)-1, -1, -1):
                add_var+=1
                arr[lst[i]]+=add_var
    for rng in range(len(struct_negative)):
        lst = struct_negative[rng]
        for i in range(len(lst)-1, -1,-1):
            add_var+=1
            arr[lst[i]]+=add_var
else:
    for rng in range(len(struct)-1, -1, -1):
        lst = struct[rng]
        if lst!=[]:
            for i in range(len(lst)-1, -1, -1):
                add_var+=1
                arr[lst[i]]+=add_var
print(arr)
