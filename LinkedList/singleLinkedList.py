"""
    Single link list implement
"""


class LinkedListUnderflow(ValueError):
    pass


class LNode:
    """
        link node
    """
    def __init__(self, elem, next_=None):
        """
            naming next_ is in case conflict with the system function `next`
        """
        self.elem = elem
        self.next = next_


class LList:
    """
        linked list class
    """
    def __init__(self):
        """
            _head is the first elem of linkedlist
        """
        self._head = None
        self.size = 0

    def get_size(self):
        p = self._head
        count = 0
        while p is not None:
            count = count + 1
            p = p.next

        self.size = count
        return count

    def prepend(self, elem):
        """
            insert the elem as the head and set his next is the currently head
        """
        self._head = LNode(elem, self._head)

    def pop(self):
        """
            remove head from list
        """
        if self._head is None:
            raise LinkedListUnderflow('list is empty.')
        head_elem = self._head
        self._head = head_elem.next
        return head_elem

    def pop_last(self):
        """
            remove last element,
            we need to find which element, it's p.next.next is None.
            The last second element, it's do not have next.next object
        """
        if self._head is None:
            raise LinkedListUnderflow('list is empty.')

        p = self._head
        # list only have 1 element
        if p.next is None:
            e = p.elem
            self._head = None
            return e

        # list exist more than 1 element, find the last second element
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def append(self, elem):
        """
            insert elem as the last elem,
            loop all elem and find last elem, then set next for last elem
        """
        if self._head is None:
            self._head = LNode(elem)
            return

        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def preview(self):
        """
            preview the all list
        """
        p = self._head
        while p is not None:
            print(p.elem)
            p = p.next

    def elements(self):
        """
            return iterator element
        """
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def check_elem_exist(self, elem):
        """
            check elem exist in list or not
        """
        p = self._head
        founded = False
        while p is not None and not founded:
            if p.elem == elem:
                founded = True
            else:
                p = p.next

        return founded

    def filters(self, lambda_func):
        """
            Using lambda function process data
        """
        p = self._head
        while p is not None:
            if lambda_func(p.elem):
                yield p.elem
            p = p.next


# ll = LList()
# for i in range(0, 10):
#     ll.append(i)

# print('size is {0}'.format(ll.get_size()))

# ll.preview()

# els = ll.elements()
# for i in els:
#     print(i)

# print(ll.check_elem_exist(9))