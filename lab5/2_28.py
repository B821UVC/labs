'''
28. Две функции у = f(x) и у = f(x) заданы таблично на отрезке
[А, В]. Необходимо:
a) определить, является ли каждая их этих функций монотонно
убывающей или монотонно возрастающей на заданном отрезке. Про-
верку монотонности функции оформить в виде метода;
б) найти все интервалы монотонности. Использовать метод;
b) найти самый длинный интервал монотонности. Использовать
метод.'''

f1 = [10, 34, 77, 98, 115, 186, 260]
f2 = [511, 319, 200, 140, 58, 34, 7]

f_test=[15, 90, 70, 500, 71, 0, 0]


def is_monotonic_increasing(func_values):
    for i in range(len(func_values) - 1):
        if func_values[i + 1] < func_values[i]:
            return False
    return True

def is_monotonic_decreasing(func_values):
    for i in range(len(func_values) - 1):
        if func_values[i + 1] > func_values[i]:
            return False
    return True



def find_intervals_of_monotonicity(func_values):
    intervals = []
    types=[3,]
    current_interval = [func_values[0]]
    monotonic_type = None
    
    for i in range(len(func_values)-1):
        if func_values[i+1] > func_values[i]:
            if monotonic_type != 1:
                if current_interval:
                    intervals.append(current_interval)
                    types.append("возрастает")
                current_interval = [func_values[i]]
                monotonic_type = 1
            current_interval.append(func_values[i+1])
        elif func_values[i+1] < func_values[i]:
            if monotonic_type != 0:
                if current_interval:
                    intervals.append(current_interval)
                    types.append("убывает")
                current_interval = [func_values[i]]
                monotonic_type = 0
            current_interval.append(func_values[i+1])
        else:
            continue
    
    if current_interval:
        intervals.append(current_interval)
    
    return intervals, types

def longest_monotonic_interval(intervals):
    res=0
    for i in intervals:
        if len(i)>res:
            res = len(i)
    return res

def check_f(vals):
    if is_monotonic_increasing(vals):
        print("функция монотонно возрастает")
    elif is_monotonic_decreasing(vals):
        print("функция монотонно убывает")
    else:
        print("функция не является ни монотонно убывающей, ни монотонно возрастающей")
    intervals, types = find_intervals_of_monotonicity(vals)
    print("Интервалы функции:")
    for i in range(1, len(intervals)):
        print(intervals[i], types[i])
    print(f"длина самого длинного интервала {longest_monotonic_interval(intervals)}")

check_f(f1)
check_f(f2)
check_f(f_test)