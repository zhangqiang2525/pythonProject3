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
        if self.is_empty():
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
            print('所插入的位置大于当前链表长度')
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
            print('链表为空')
            return
        else:
            pre = None
            cur = self.__head
            while cur is not None:
                if cur.value != item:
                    pre = cur
                    cur = cur.next
                else:
                    if cur == self.__head:
                        self.__head = self.__head.next
                        break
                    else:
                        pre.next = cur.next
                        break

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.value == item:
                return True
            else:
                cur = cur.next

        return False

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.value, end=' ')
            cur = cur.next
        print()

    def reversed(self):
        cur = self.__head
        if cur is None or cur.next is None:
            return cur

        else:
            pre = None
            h = self.__head
            while cur:
                h = cur
                next_node = cur.next
                cur.next = pre
                pre = cur
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
print(single_obj.search(0))
single_obj.remove(2)
single_obj.travel()
p = single_obj.reversed()
while p:
    print(p.value, end=' ')
    p = p.next
