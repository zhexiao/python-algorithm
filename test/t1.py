def quick_sort(data):
    if len(data) <= 1:
        return data

    # 拿到中间值并把中间值从数组中去掉
    mid_position = len(data)//2
    mid_val = data[mid_position]
    data.pop(mid_position)

    # 定义所有小于中间值的数组和所有大于中间值的数组
    left_arr = []
    right_arr = []

    for v in data:
        if v < mid_val:
            left_arr.append(v)
        else:
            right_arr.append(v)

    return quick_sort(left_arr) + [mid_val] + quick_sort(right_arr)

data = [20, 5, 10, 4, 12]
sort_data = quick_sort(data)
print(sort_data)