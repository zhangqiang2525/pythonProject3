class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class single_link_list(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        """
        头插法
        :param item:
        :return:
        """
        node = Node(item)
        if self.__head is None:
            self.__head = node

        else:
            node.next = self.__head
            self.__head = node

    def append(self, item):
        """
        尾插法
        :param item:
        :return:
        """
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next

            cur.next = node

    def insert(self, pos, item):
        """
        任意位置插入元素
        :param pos:
        :param item:
        :return:
        """
        if pos <= 0:
            self.add(item)

        elif pos == self.length():
            self.append(item)

        elif pos > self.length():
            print('您插入的位置大于当前链表长度')
            return

        else:
            node = Node(item)
            count = 0
            cur = self.__head
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):








    def length(self):
        pass