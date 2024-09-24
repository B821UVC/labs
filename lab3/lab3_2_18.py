'''Если максимальный среди элементов с четными индексами
больше максимального среди элементов с нечетными индексами, то
заменить нулями элементы первой половины массива, иначе - элементы второй половины.'''

arr = [0, 3, 99, 15, 16, 55, 44, -31, 500]
mx_odd =0
mx_even = 0

for ps,i in enumerate(arr):
    if ps%2==0:
        mx_even = max(mx_even, i)
    else:
        mx_odd  = max(mx_odd, i)
is_arr_odd=False
if len(arr)%2!=0:
    d = arr//2+1
    is_arr_odd = True
else:
    d = arr//2

if is_arr_odd:
    if mx_even>mx_odd:
        arr = [0]*d + arr[d:]
    else:
        arr = arr[:d] + [0]*d-1

else:
    if mx_even>mx_odd:
        arr = [0]*d + arr[2*d:]
    else:
        arr = arr[:d] + [0]*d
