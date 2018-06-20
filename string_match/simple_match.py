"""
字符串的 朴素匹配

效率不好的原因是：执行中出现回溯，每次匹配失败都需要重置i=0从头匹配
"""
a = 'abcddeabdeda'
b = 'dea'


def naive_matching(strs, match_str):
    m, n = len(match_str), len(strs)
    i, j = 0, 0

    while i < m and j < n:
        if match_str[i] == strs[j]:
            print('yes', i, j)
            i, j = i + 1, j + 1
        else:
            # 整个字符串匹配到了位置j时，前面正确的匹配了i个元素；
            # 如果在j位置失败，则下次匹配开始的位置是 j - i + 1
            print('no', i, j)
            i, j = 0, j + 1 - i

        # 如果i的长度与我们需要匹配的字符串长度一样，那就说明匹配成功了
        if i == m:
            print(j - m)
            return j - m
    return -1


if __name__ == '__main__':
    naive_matching(a, b)
