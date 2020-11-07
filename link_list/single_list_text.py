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
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)

        elif pos == self.length():
            self.append(item)

        elif pos > self.length():
            print('您插入的位置大于当前链表的长度')
            return

        else:
            cur = self.__head
            count = 0
            node = Node(item)
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            print('链表为空不能执行该操作')
        else:
            prev = None
            cur = self.__head
            while cur:
                if cur.value != item:
                    prev = cur
                    cur = cur.next
                else:
                    if cur == self.__head:
                        self.__head = cur.next
                        break
                    else:
                        prev.next = cur.next
                        break

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        cur = self.__head
        while cur:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.value, end=' ')
            cur = cur.next
        print()

    def reversed(self):
        if self.is_empty():
            print('链表为空不能执行该操作')
            return
        else:
            prev, cur, h = None, self.__head, self.__head
            while cur:
                h = cur
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
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
print(single_obj.length())
print(single_obj.search(0))
single_obj.remove(2)
single_obj.travel()
p = single_obj.reversed()
while p:
    print(p.value, end=' ')
    p = p.next
