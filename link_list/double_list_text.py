class Node(object):
    def __init__(self,value):
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
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            node.prev = cur
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)

        elif pos == self.length():
            self.append(item)

        elif pos > self.length():
            print('您插入的位置大于当前链表长度')
            return

        else:
            count = 0
            node = Node(item)
            cur = self.__head
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            print('链表为空不能执行该操作')
            return
        else:
            cur = self.__head
            if cur.value == item:
                if cur.next is None:
                    self.__head = None
                else:
                    cur.next.prev = None
                    self.__head = cur.next
                return
            while cur is not None:
                if cur.value == item:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False

    def length(self):
        count = 0
        cur = self.__head
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.value, end=' ')
            cur = cur.next
        print()

    def reverse(self):
        if self.is_empty():
            print('链表为空不能执行该操作')
            return
        pre = None
        cur = self.__head
        while cur:
            next_node = cur.next
            cur.next = pre
            cur.prev = next_node

            pre = cur
            cur = next_node
        self.__head = pre

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
single_obj.reverse()
single_obj.travel()
