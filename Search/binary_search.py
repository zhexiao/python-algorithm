"""
Binary Search
二分法检索（binary search）又称折半检索，
二分法检索的基本思想是设字典中的元素从小到大有序地存放在数组（array）中
首先将给定值key与字典中间位置上元素的关键码(key)比较，如果相等，则检索成功；
否则，若key小，则在字典前半部分中继续进行二分法检索;
若key大，则在字典后半部分中继续进行二分法检索。
二分法检索是一种效率较高的检索方法，要求字典在顺序表中按关键码排序。
"""


def binary_search(search_lists, search_key):
    """
    二分查找
    :param search_lists: search lists array 
    :param search_key: number for search
    :return: 
    """
    # low代表数组里面的最低位置，high代表数组里面的最高位置
    low = 0
    high = len(search_lists) - 1

    while high >= low:
        # 得到中间位置和值
        mid = int((low + high) / 2)
        guess = search_lists[mid]

        if guess == search_key:
            return mid

        if guess > search_key:
            high = mid - 1
        else:
            low = mid + 1


li = [1, 3, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9]
print(binary_search(li, 7))
