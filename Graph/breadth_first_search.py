"""
宽度优先搜索/广度优先搜索

下面的例子是找到会打篮球的朋友，我有3个朋友（"alice", "bob", "claire"），bob又有2个
朋友（"anuj", "peggy"），依次类推
"""
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def checl_right_person(person):
    return person == 'jonny'


def search(name):
    # 创建搜索队列
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        # 取出其中的第一个人
        person = search_queue.popleft()
        if not person in searched:
            # 如果是正确要找的，返回
            if checl_right_person(person):
                print(person + " is a basketball player")
                return True
            # 如果不是要找的，则把他的朋友加到这个search_queue搜索队列中
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
