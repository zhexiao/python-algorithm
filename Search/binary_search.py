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
    Binary search
    :param search_lists: search lists array 
    :param search_key: number for search
    :return: 
    """
    min_position = 0
    max_position = len(search_lists) - 1

    i = 0
    while max_position >= min_position:
        i = i + 1
        # get mid position
        mid_position = int((min_position + max_position) / 2)

        # compare the search key with the mid value
        if search_key == search_lists[mid_position]:
            print("find {0} at index {1} in {2} times.".format(
                search_key,
                mid_position,
                i
            ))
            break
        else:
            # value before the middle, new search should from (0 ~ mid-1)
            if search_key < search_lists[mid_position]:
                max_position = mid_position - 1
            # value after the middle, new search should from (mid+1 ~ max)
            else:
                min_position = mid_position + 1

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_search(li, 7)
