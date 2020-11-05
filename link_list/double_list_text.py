class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Double_link_list(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node

        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos == self.length():
            self.append(item)

        elif pos > self.length():
            print('您插入的位置大于当前链表的长度')
            return
        else:
            node = Node(item)
            count = 0
            current = self.__head
            while count < (pos - 1):
                count += 1
                current = current.next
            node.prev = current
            node.next = current.next
            current.next.prev = node
            current.next = node

    def remove(self, item):
        if self.is_empty():
            print('链表当前为空不能执行该操作')
            return
        else:
            current = self.__head
            if current.value == item:
                if current.next is None:
                    self.__head = None
                else:
                    current.next.prev = None
                    self.__head = current.next
                return
            while current is not None:
                if current.value == item:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    break
                current = current.next

    def search(self, item):
        current = self.__head
        while current is not None:
            if current.value == item:
                return True
            else:
                current = current.next
        return False

    def length(self):
        count = 0
        current = self.__head
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        current = self.__head
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print()


single_obj = Double_link_list()
print(single_obj.is_empty())
print(single_obj.length())
single_obj.append(1)
single_obj.append(2)
single_obj.append(3)
single_obj.append(4)
single_obj.append(5)
single_obj.travel()
single_obj.add(-1)
single_obj.travel()
single_obj.insert(-1, -2)
single_obj.travel()
single_obj.insert(2, 0)
single_obj.travel()
print(f'链表的长度为{single_obj.length()}')
print(single_obj.search(0))
single_obj.remove(2)
single_obj.travel()
