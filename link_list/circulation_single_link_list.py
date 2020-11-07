class Node(object):
    def __init__(self, value):
        """单循环链表结点"""
        self.value = value
        self.next = None


class SinglyLinkedCircularList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """求链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1  # 下方循环退出时，链表至少有一个结点
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环时，cur指向最后一个结点
        print(cur.elem)

    def add(self, elem):
        """向链表头部添加元素"""
        node = Node(elem)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, elem):
        """向链表尾部添加元素"""
        node = Node(elem)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, elem):
        """向链表位置pos处插入元素

        Args:
            pos: 插入的位置，从0开始计数
            elem: 插入的元素
        """
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length() - 1):
            self.append(elem)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 退出循环，pre指向插入位置的前一个结点
            node = Node(elem)
            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        """删除链表中第一个为elem的元素"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == elem:
                # 头结点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    rear.next = cur.next
                    self.__head = cur.next
                else:  # 中间结点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环, cur指向尾结点
        if cur.elem == elem:
            # 链表中只有一个结点
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, elem):
        """查找链表中是否存在元素elem"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == elem:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == elem:
            return True
        return False