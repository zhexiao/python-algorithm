"""
选择排序：
选择排序是一种灵巧的算法，但其速度不是很快。

1. 先编写一个用于找到数组中最小元素的函数
2. 使用步骤1的函数完成排序
"""


def find_smallest(arr):
    """
    找到数组中的最小值
    :param arr:
    :return:
    """
    smallest_idx = 0
    smallest = arr[smallest_idx]

    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest_idx = i
            smallest = arr[i]

    return smallest_idx


def selection_sort(arr):
    """
    选择排序
    :param arr:
    :return:
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        # 使用pop，把已经找到的值从老的数据中剔除掉并返回
        new_arr.append(arr.pop(smallest))

    return new_arr


arr = [99, 53, 66, 23, 3, 22, 1, 45, 120, 69]
print(selection_sort(arr))
