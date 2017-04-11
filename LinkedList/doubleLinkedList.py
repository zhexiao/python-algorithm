# -*- coding: UTF-8 -*-
"""
    双链表类
"""
from singleLinkedList import LinkedListUnderflow


class DLinkNode:
    """
        双链表的结点可以基于单链表的结点，但是由于双链表结点多了一个反向指针指向前一个结点
        所以需要对链表的属性进行修改
    """

    def __init__(self, elem, prev=None, next_=None):
        """
            使用next_是为了防止与内置函数混淆
        """
        self.elem = elem
        self.prev = prev
        self.next = next_


class DLList:

    def __init__(self):
        self._head = None
        self._rear = None
        self.size = 0

    def is_empty(self):
        """
            检查链表是否为空
        """
        return self._head is None

    def get_size(self):
        count = 0
        node_ = self._head
        while node_ is not None:
            count = count + 1
            node_ = node_.next

        self.size = count
        return count

    def prepend(self, elem):
        """
            在插入数据到链表首端
        """
        # 首端插入，则它的next_永远指向原来的_head
        node_ = DLinkNode(elem, None, self._head)

        if self.is_empty():
            # 则新插入的元素及时_head也是_rear
            self._rear = node_
        else:
            # 则需要更新原来_head的prev指针
            node_.next.prev = node_

        self._head = node_

    def append(self, elem):
        """
            插入数据到链表尾端
        """
        # 末端插入，则新结点的_next为None, prev应该指向原来的_rear
        node_ = DLinkNode(elem, self._rear, None)
        if self.is_empty():
            # 则新的的结点既是头又是为
            self._head = node_
        else:
            # 则需要更新原_rear结点的next_指针
            node_.prev.next = node_
        self._rear = node_

    def pop(self):
        """
            弹出第一个结点
        """
        if self.is_empty():
            raise LinkedListUnderflow('链表为空，不能处理弹出方法。')
        else:
            node_elem = self._head.elem

            self._head = self._head.next
            if self._head is not None:
                # 如果新的_head结点存在，则更新新head结点的prev指针
                self._head.prev = None

            return node_elem

    def pop_last(self):
        """
            弹出最后一个结点
        """
        if self.is_empty():
            raise LinkedListUnderflow('链表为空，不能处理弹出方法。')
        else:
            node_elem = self._rear.elem

            self._rear = self._rear.prev
            if self._rear is not None:
                self._rear.next = None
            else:
                # 这里设置_head是因为如果_rear为none, 则证明弹出的元素是链表里面的最后一个元素，设置_head为None是为了保证is_empty方法顺利的执行。
                self._head = None

            return node_elem

    def preview(self):
        """
            预览列表数据
        """
        if self.is_empty():
            raise LinkedListUnderflow('链表为空。')

        node_ = self._head
        while node_ is not None:
            print(node_.elem)
            node_ = node_.next


# dll = DLList()
# for i in range(0, 20):
#     dll.append(i)

# print('size is {0}'.format(dll.get_size()))

# print('------------------')
# dll.preview()
# dll.pop()
# dll.pop_last()
# print('------------------')
# dll.preview()
