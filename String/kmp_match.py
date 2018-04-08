"""
KMP算法 匹配中不回溯

简单点就是在匹配失败的时候把模式串前移若干位置，用模式串里匹配失败的字符之前的某个字符与目标串
中匹配失败的字符比较。

KMP算法的精髓就是开发了一套分析和记录模式串信息的机制，而后借助得到的信息加速匹配。
匹配过程：
1. 当匹配到第一个c失败时，由于已知模式串p_str的前2个字符不同，KMP算法直接把模式串移动2个位置，
模式串开头a直接移动到c失败的位置。
2. 模式串匹配到最后的c时失败，由于最后c之前的字符是a，首字符也是a，而且c与a直接的字符不同，不可能
有匹配，所以KMP算法直接把模式串的b移动到刚才最后c匹配失败的位置。
3. 匹配成功了

"""
t_str = 'BBC ABCDAB ABCDABCDABDEFGD'
p_str = 'ABCDABD'


def kmp_match(target_str, pattern_str, pattern_next):
    """
    KMP查找函数
    :param target_str: 目标字符串
    :param pattern_str: 模式匹配字符串
    :param pattern_next: 假设pattern_str在第i个字符（p_s[i]）匹配失败，
    则证明前面已经有k个字符在target_str已经匹配成功了即p_s[k](0=<k<i)，
    这说明目标字符串target_str中存在i个字符等于p_s[0]p_s[1]...p_s[i-1]，
    这也就是说对p_s中的每个i，都有在target_str中对应的下标k，即p_s[i]=t_s[k]。
    假设模式匹配字符串的长度为m，则现在需要对每个i(0=<i<m)计算出对应的k并将其保存起来以便
    匹配的时候使用，为此我们可以考虑用一个长为m的表p_next,用p_next[i]记录k值，
    默认第一次匹配可以将p_next[0]设置为-1,即p_next[0]=-1
    :return:
    """
    t_count, p_count = 0, 0
    t_len, p_len = len(target_str), len(pattern_str)

    while t_count < t_len and p_count < p_len:
        # 说明字符匹配成功，则继续比较下一个字符
        if p_count == -1 or target_str[t_count] == pattern_str[p_count]:
            t_count, p_count = t_count + 1, p_count + 1
        # 如果匹配失败，则从p_next中找取得pattern_str下一字符的位置
        else:
            p_count = pattern_next[p_count]
    return -1


def gen_pattern_next(p):
    i, k = 0, -1
    p_len = len(p)
    p_next = [-1] * p_len

    while i < p_len - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            p_next[i] = k
        else:
            k = p_next[k]
    return p_next


p_next_list = gen_pattern_next(p_str)
kmp_match(t_str, p_str, p_next_list)
