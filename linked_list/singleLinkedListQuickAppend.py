from singleLinkedList import LinkedListUnderflow, LNode, LList


class LListQuickAppend(LList):
    """
        Quickly append data by avoid loop all elements
    """

    def __init__(self):
        """
            _rear is the pointer of the last node
        """
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        """
            prepend the elem as the head,
            the pointer of the last node is not change
        """
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        """
            append elem to the list, we need to modify the _rear
        """
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            r = self._rear
            r.next = LNode(elem)
            self._rear = r.next

    def pop_last(self):
        """
            remove the last node, need to modify _rear
        """
        if self._head is None:
            raise LinkedListUnderflow('list is empty')

        # only 1 element
        if self._head == self._rear:
            e = self._head.elem
            self._head = None
            return e

        # find the last second node and set _rear to the last second node
        p = self._head
        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        self._rear = p
        return e


ll = LListQuickAppend()
for i in range(0, 30):
    ll.append(i)

print('size is {0}'.format(ll.get_size()))

# using lambda function only get the element which can divide by 2
for x in ll.filters(lambda y: y % 2 == 0):
    print(x)
