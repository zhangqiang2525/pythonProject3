class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Cir_single_link_list(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            # 节点的next指向自己
            node.next = node

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node

        else:
            cur = self.__head
            while cur:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)

        elif pos == self.length():
            self.append(item)

        elif pos > self.length():
            print('插入位置大于链表当前长度')
            return
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (pos - 1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            print('链表为空不能执行该操作')
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.value == item:
                if cur == self.__head:
                    last = self.__head
                    while last.next != self.__head:
                        last = last.next
                    last.next = cur.next
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.next == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            print('链表为空，您查找的元素不存在')
        cur = self.__head
        while cur.next != self.__head:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        if cur.value == item:
            return True

        return False

    def travel(self):
        cur = self.__head
        while cur.next != self.__head:
            print(cur.value, end=' ')
            cur = cur.next
        print(cur.value)
        print()

    def length(self):
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count


