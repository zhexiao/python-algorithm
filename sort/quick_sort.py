"""
快速排序：
快速排序是一种效率很高的排序算法，使用了分而治之（D&C)。

对排序算法来说，最简单的数组什么样呢？就是根本不需要排序的数组。
因此，基线条件为数组为空或只包含一个元素。

1. 从数组中选择一个元素，这个元素被称为基准值（pivot）。
2. 找出比基准值小的元素以及比基准值大的元素，这被称为分区（partitioning）。
3. 对这两个分区的子数组进行快速排序。

注：快速排序的情况比较棘手，在最糟情况下，其运行时间为O(n^2)。
这种情况发生是因为：
快速排序的性能高度依赖于你选择的基准值，假设你总是将第一个元素用作基准值，且要处
理的数组是有序的。由于快速排序算法不检查输入数组是否有序，因此它依然尝试对其进行排序，
数组并没有被分成两半，相反，其中一个子数组始终为空，这导致调用栈非常长。

总结：
最佳情况也是平均情况。只要你每次都随机地选择一个数组元素作为基准值，
快速排序的平均运行时间就将为O(n log n)。快速排序是最快的排序算法之一，也是D&C典范。
"""


def quick_sort(arr):
    # 基线条件：数组为空或只包含一个元素的数组是“有序”的
    if len(arr) <= 1:
        return arr
    else:
        # 定义大于基准值和小于基准值的2个子数组
        less_arr = []
        grater_arr = []

        # 选一个基准值
        pivot = arr[0]

        # 这个range从1开始，是因为arr[0]的值作为了基准值
        for i in range(1, len(arr)):
            num = arr[i]
            if num > pivot:
                grater_arr.append(num)
            else:
                less_arr.append(num)

        return quick_sort(less_arr) + [pivot] + quick_sort(grater_arr)


arr = [22, 554, 61, 123, 15, 32, 100, 56, 799]
print(quick_sort(arr))
