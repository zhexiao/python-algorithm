"""
归并排序是建立在归并操作上的一种有效的排序算法,
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
若将两个有序表合并成一个有序表，称为二路归并。

归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，
再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。

一般用于对总体无序，但是各子项相对有序的数列
"""


def merge(left, right):
    """
    对二分后的序列进行排序合并
    :param left: 
    :param right: 
    :return: 排序后的序列
    """

    i, j = 0, 0
    result = []
    while len(left) > i and len(right) > j:
        if right[j] >= left[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def merge_sort(lists):
    """
    归并排序
    :param lists: 需要排序的序列
    :return: 排序后的序列
    """
    if len(lists) <= 1:
        return lists

    # 得到中间长度，将序列二分
    mid_len = int(len(lists)/2)
    left = merge_sort(lists[:mid_len])
    right = merge_sort(lists[mid_len:])

    # 将二分后的序列进行排序
    return merge(left, right)

sort_lists = [22, 11, 55, 33, 66, 123, 2, 123123, 2155, 1231231]
print(merge_sort(sort_lists))
