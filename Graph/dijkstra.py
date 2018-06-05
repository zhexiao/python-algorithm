"""
狄克斯特拉算法：
使用这个算法可以寻找最短路径，示例如图2。

算法步骤：
1. 用散列表存储每个节点的邻居和前往邻居的开销
2. 用散列表存储每个节点的开销，节点的开销指的是从起点出发前往该节点需要多长时间
3. 存储父节点的散列表
4. 需要一个数组，用于记录处理过的节点，因为对于同一个节点，你不用处理多次

注意：如果有负权边，就不能使用狄克斯特拉算法。在包含负权边的图中，
要找出最短路径，可使用另一种算法——贝尔曼福德算法（Bellman-Ford algorithm）。
"""

# 定义每个节点的邻居和前往该邻居的开销
graph = {}
graph['start'] = {
    'a': 6,
    'b': 2
}
graph['a'] = {
    'end': '1'
}
graph['b'] = {
    'a': 3,
    'end': 5
}
graph['end'] = {}

# 存储每个节点的开销，这是从起点到每个节点的开销，未知开销用无穷大的表示
costs = {
    'a': 6,
    'b': 2,
    'end': float('inf')  # 这个表示无穷大
}

# 存储父节点的散列表
parents = {
    'a': 'start',
    'b': 'start',
    'end': None
}

# 需要一个数组，用于记录处理过的节点，因为对于同一个节点，你不用处理多次
processed = []


# 从未处理的节点中找到开销最小的节点
def find_lowest_cost_node(costs):
    """
    找到最小的开销节点
    :param costs:
    :return:
    """
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]

    # 获得当前节点的所有邻居
    neighbors = graph[node]

    for n in neighbors.keys():
        # 得到当前节点到其某个邻居的开销
        new_cost = float(cost) + float(neighbors[n])
        # 如果经当前节点前往该邻居更近
        if new_cost < costs[n]:
            # 就更新该邻居的开销
            costs[n] = new_cost
            # 同时将该邻居的父节点设置为当前节点
            parents[n] = node
    # 将当前节点标记为处理过
    processed.append(node)
    # 找出接下来要处理的节点，并循环
    node = find_lowest_cost_node(costs)

print(parents)
