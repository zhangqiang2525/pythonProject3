class Node(object):
    """双向链表节点"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    """双向链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self.__head
            # 将_head的头节点的prev指向node
            self.__head.prev = node
            # 将_head 指向node
            self.__head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self.__head = node
        else:
            # 移动到链表尾部
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def search(self, item):
        """查找元素是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos == (self.length()):
            self.append(item)

        elif pos > self.length():
            print('您插入的位置大于当前链表的位置')
            return
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self.__head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next is None:
                    # 如果链表只有这一个节点
                    self.__head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur.next.prev = None
                    # 将_head指向第二个节点
                    self.__head = cur.next
                return
            while cur is not None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

    def length(self):
        """返回链表的长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next
        print()

    def reverse(self):
        """
        将链表头尾反转
        :return:
        """
        pre = None
        current = self.__head  # 将头节点保存在current中

        # 当链表为非空的时候，需要执行相应反转的操作
        if self.is_empty():
            print('链表为空不能执行当前操作')
            return
        # 分别将相邻的两个节点的前驱后继关系进行反转
        while current:
            next_node = current.next  # 将下一个节点保存在next_node中
            current.next = pre  # 由于反转链表，因此头节点反转后，成为尾节点，应该指向None
            current.prev = next_node  # 尾节点的前驱应指向原本的后继

            pre = current  # 更新prev，向后移动
            current = next_node  # 更新current，向后移动
        # 到达链表尾部时，需要特殊处理
        self.__head = pre


single_obj = DLinkList()
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
single_obj.travel()