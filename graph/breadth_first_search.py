"""
宽度优先搜索/广度优先搜索

查找是否存在抵达目的地G的路线，如图1
"""
from collections import deque

graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['E']
graph['C'] = ['D']
graph['D'] = ['G']
graph['E'] = ['D', 'F']
graph['F'] = ['G']
graph['G'] = []


def check_dest(address):
    return address == 'G'


def search(addr):
    # 创建搜索队列
    search_queue = deque()
    search_queue += graph[addr]

    # 保存已经被搜索过的地址
    searched_list = []
    while search_queue:
        addr_name = search_queue.popleft()
        if addr_name not in searched_list:
            # 如果找到了目的地
            if check_dest(addr_name):
                print('找到了路径')
                return True
            # 如果没找到，则把他的邻居也加入到搜索队列中
            else:
                neighbor_addr_list = graph[addr_name]
                search_queue += neighbor_addr_list

                # 防止被重复搜索
                searched_list.append(addr_name)


search('A')
