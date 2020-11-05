class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Single_link_list(object):
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

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)

        elif pos == self.length():
            self.append(item)

        elif pos > self.length():
            print('您插入的位置大于当前链表的长度')
            return

        else:
            count = 0
            node = Node(item)
            current = self.__head
            while count < (pos - 1):
                count += 1
                current = current.next
            node.next = current.next
            current.next = node

    def remove(self, item):
        if self.is_empty():
            print('当前链表为空，不能执行该操作')
            return
        else:
            prev = None
            current = self.__head
            while current is not None:
                if current.value != item:
                    prev = current
                    current = current.next
                else:
                    if self.__head == item:
                        self.__head = current.next
                        break
                    else:
                        prev.next = current.next
                        break

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
        print('')

    def reversed(self):
        if self.__head is None or self.__head.next is None:
            return self.__head
        prev, current, h = None, self.__head, self.__head
        while current:
            h = current
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return h








single_obj = Single_link_list()
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
print(single_obj.search(0))
single_obj.remove(2)
single_obj.travel()
p = single_obj.reversed()
while p:
    print(p.value, end=' ')
    p = p.next
