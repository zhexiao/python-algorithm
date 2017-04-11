# -*- coding: UTF-8 -*-
"""
    循环双链表
    表首结点的prev指向表尾结点
    表尾结点的next指向表首结点
"""
from doubleLinkedList import DLinkNode, DLList, LinkedListUnderflow


class DLListCycle(DLList):
    """
        循环双链表，基于双链表，只需要在插入或者删除时对表尾或者表首指针进行修改
    """

    def __init__(self):
        DLList.__init__(self)

    def get_size(self):
        """
            获取链表的数量
        """
        count = 0
        node_ = self._head
        while True:
            count = count + 1
            node_ = node_.next
            if node_ is self._head:
                break

        self.size = count
        return count

    def prepend(self, elem):
        """
            插入的元素为_head结点
        """
        node_ = DLinkNode(elem, self._rear, self._head)
        if self.is_empty():
            # 则表首即为表尾，自我创建循环
            self._head = node_
            self._rear = node_
            self._rear.next = node_
            self._head.prev = node_
        else:
            # 则新结点的prev指向_rear，更新最后一个结点的next和以前_head结点的prev
            self._head = node_
            self._head.prev = self._rear
            self._rear.next = node_
            node_.next.prev = node_

    def append(self, elem):
        """
            插入元素为_rear结点
        """
        node_ = DLinkNode(elem, self._rear, self._head)
        if self.is_empty():
            # 则表首即为表尾，自我创建循环
            self._head = node_
            self._rear = node_
            self._head.prev = node_
            self._rear.next = node_
        else:
            # 则新结点的_next指向_head，更新头部结点的prev指向新的结点，更新以前_rear结点next指向新结点
            self._rear = node_
            self._rear.next = self._head
            self._head.prev = node_
            node_.prev.next = node_

    def pop(self):
        """
            弹出head结点
        """
        if self.is_empty():
            raise LinkedListUnderflow('空链表，无法弹出。')

        node_elem = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            # 则更新_rear的next指向新的head结点
            self._rear.next = self._head
            # 更新新head的prev指向表尾结点
            self._head.prev = self._rear
        else:
            self._head = None
            self._rear = None

        return node_elem

    def pop_last(self):
        """
            弹出_rear结点
        """
        if self.is_empty():
            raise LinkedListUnderflow('空链表，无法弹出。')

        node_elem = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is not None:
            # 更新新的_rear结点的next指向_head
            self._rear.next = self._head
            # 更新_head的prev指向新的_rear
            self._head.prev = self._rear
        else:
            self._head = None
            self._rear = None

        return node_elem

    def preview(self):
        """
            预览所有数据
        """
        node_ = self._head
        while True:
            print(node_.elem)
            node_ = node_.next
            if node_ is self._head:
                break


dllcycle = DLListCycle()
for i in range(0, 20):
    dllcycle.append(i)

print('size is {0}'.format(dllcycle.get_size()))

print('------------------')
dllcycle.preview()
dllcycle.pop()
dllcycle.pop_last()
print('------------------')
dllcycle.preview()
