"""
狄克斯特拉算法：
使用这个算法可以寻找最短路径，示例如图3。

算法步骤：
1. 用散列表存储每个节点的邻居和前往邻居的开销
2. 用散列表存储每个节点的开销，节点的开销指的是从起点出发前往该节点需要多长时间
3. 存储父节点的散列表
4. 需要一个数组，用于记录处理过的节点，因为对于同一个节点，你不用处理多次
"""

# 记录每个节点的邻居以及到该邻居的开销
graph = {
    'start': {
        'a': 5,
        'b': 2
    },
    'a': {
        'c': 2,
        'd': 4
    },
    'b': {
        'a': 8,
        'c': 7
    },
    'c': {
        'end': 1
    },
    'd': {
        'c': 6,
        'end': 3
    },
    'end': {}
}

# 记录从起点到每个节点的开销，开销未知我们使用无穷大
costs = {
    'a': 5,
    'b': 2,
    'c': float('inf'),
    'd': float('inf'),
    'end': float('inf')
}

# 记录从起点到每个节点的父节点
parents = {
    'a': 'start',
    'b': 'start',
    'c': None,
    'd': None,
    'end': None
}

# 记录已经被处理过的节点
processed = []


def get_lowest_cost_node(costs):
    """
    拿到开销最小的节点
    :param costs:
    :return:
    """
    lowest_cost = float('inf')
    lowest_node = None

    for node, cost in costs.items():
        # 如果节点的开销是最小的开销并且没有被处理过
        if cost < lowest_cost and node not in processed:
            lowest_node = node
            lowest_cost = cost

    return lowest_node


def get_short_path():
    """
    计算得出最短路径
    :return:
    """
    current_node = get_lowest_cost_node(costs)
    while current_node is not None:
        # 当前运行节点的开销值
        current_node_cost = costs[current_node]
        # 当前运行节点的邻居节点
        neighbor_nodes = graph[current_node]

        for nbor_node, nbor_cost in neighbor_nodes.items():
            # 计算当前节点到该邻居节点的开销
            to_nbor_cost = current_node_cost + nbor_cost

            # 如果开销小于costs表中的开销，则更新记录
            if to_nbor_cost < costs[nbor_node]:
                # 更新邻居节点的开销
                costs[nbor_node] = to_nbor_cost
                # 更新邻居节点的父节点
                parents[nbor_node] = current_node

        # 循环完毕，将current_node加入已经计算过的数组中不再重复计算
        processed.append(current_node)
        current_node = get_lowest_cost_node(costs)


if __name__ == '__main__':
    get_short_path()

    # 得到路径
    end_signal = 'end'
    while end_signal != 'start':
        end_signal = parents[end_signal]
        print(end_signal)
