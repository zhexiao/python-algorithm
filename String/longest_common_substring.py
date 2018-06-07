"""
最长公共子串

示例：如图1

我们可以用动态规划填充网格来解决问题，单元格中的值通常就是你要优化的值。
在这个例子中，单元格的值就是两个字符串都包含的最长子串的长度。
"""

str_1= 'blue'
str_2 = 'clues'
str_1_len = len(str_1)
str_2_len = len(str_2)

# 生成一个动态规划的默认网格，二维数组
match_grid = [
    [0 for i in range(str_1_len)] for i in range(str_2_len)
]


for n in range(str_2_len):
    for m in range(str_1_len):
        # 用str2的值与每个str1的值进行比较
        if str_2[n] == str_1[m]:
            # 如果下标从0开始，说明左上方不存在任何单元值，则默认给0
            if n == 0 or m == 0:
                pre_grid_val = 0
            # 否则去读左上方的值
            else:
                pre_grid_val = match_grid[n - 1][m - 1]

            # 左上方值+1
            match_grid[n][m] = pre_grid_val + 1
        else:
            match_grid[n][m] = 0

print(match_grid)
