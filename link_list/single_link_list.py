class Node(object):
    def __init__(self, value):
        # 存放数据元素
        self.value = value

        # 指针：指向下一个节点
        self.pointer = None


class Solution(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """
        头节点为空，则返回True 否则返回False
        :return:
        """
        return False if self.__head is None else True

    def add(self, item):
        """
        头插法：注意头插法每插入一个元素则头节点发生改变
        1、先遍历找到头节点
        2、将新节点的链接域指向头节点所指向的节点
        3、再将头节点指向新节点
        2、3顺序不能发生改变，否则会导致链表断裂
        :param item: 要插入的元素
        :return:
        """
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            node.pointer = self.__head
            self.__head = node

    def append(self, item):
        """
        尾插法：尾插法每插入一次之前都要先找None，且头节点不发生改变
        1、遍历每一个节点，找到链接域为空的节点
        2、将链接域为空的节点的链接域指向新节点
        3、重复1、2
        :param item:要插入的元素
        :return:
        """
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            # 判断节点的链接域是否为空
            while cur.pointer is not None:
                cur = cur.pointer
            # 如果为空，则当前元素的链接域直线新节点
            cur.pointer = node

    def insert(self, pos, item):
        """

        :param pos: 这里指位序，即链表的第几个位置，而实际插入时是指下标位置，
        下标是从0开始的所以需要pos-1
        :param item: 插入的元素
        :return:
        1、找到要插入位置
        2、将新节点的链接域指向当前插入位置的节点
        3、再将当前位置节点前一个节点的链接域指向新节点
        注意：2、3不能调换位置，否则会导致链表断裂
        """
        if pos <= 0:
            # 如果插入的位序小于0，即在第一个元素之前，则使用头插法
            self.add(item)

        if pos >= self.length():
            # 如果插入的位序大于当前链表长度，则使用尾插法
            self.append(item)

        else:
            node = Node(item)
            pur = self.__head
            length = 0
            while length < (pos - 1):
                length += 1
                pur = pur.pointer
            node.pointer = pur.pointer
            pur = node



    def length(self):
        """
        求链表的长度
        :return:
        """
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.pointer
        return count

