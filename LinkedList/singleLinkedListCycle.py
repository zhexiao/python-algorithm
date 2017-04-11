# -*- coding: UTF-8 -*-
"""
    循环单链表
    定义：单链表最后一个节点的next指向第一个节点
"""

from singleLinkedList import LNode, LinkedListUnderflow


class LListCycle:

    def __init__(self):
        """
            _rear是最后一个节点
        """
        self._rear = None

    def is_empty(self):
        """
            检查链表是否为空
        """
        return self._rear is None

    def prepend(self, elem):
        """
            前段插入
        """
        node = LNode(elem)
        if self.is_empty():
            # 如果空链表，则自我创建循环链表
            node.next = node
            self._rear = node
        else:
            # 新节点的next指向旧头部节点，同时更新最后一个节点的next指针
            node.next = self._rear.next
            self._rear.next = node

    def append(self, elem):
        """
            后端插入
        """
        node = LNode(elem)
        if self.is_empty():
            # 如果空链表，则自我创建循环链表
            node.next = node
            self._rear = node
        else:
            # 新节点的next指向头部，倒数第二个节点的next指向新插入的节点，重新设置_rear
            node.next = self._rear.next
            self._rear.next = node
            self._rear = node

    def pop(self):
        """
            前段弹出, 需要更新_rear的值
        """
        if self.is_empty():
            raise LinkedListUnderflow('空链表，无法弹出。')

        node_head = self._rear.next
        if node_head is self._rear:
            # 如果是自我循环即只存在一个元素
            self._rear = None
        else:
            # 更新最后节点的next指针
            self._rear.next = node_head.next

        return node_head.elem

    def preview(self):
        if self.is_empty():
            return

        node = self._rear.next
        while True:
            print(node.elem)
            # 如果当前node节点的值等于最后一个节点，则证明已经循环到了最后
            if node is self._rear:
                break
            node = node.next


ll = LListCycle()
for i in range(0, 30):
    ll.append(i)

ll.preview()
