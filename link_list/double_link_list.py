class Node(object):
    def __init__(self, value):
        self.value = value  # 保存元素
        self.next = None     # 保存下一个节点
        self.prev = None     # 保存上一个节点


class double_Link_list(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        """
        头部插入元素
        1、将新节点的链接域2（next）指向头节点所指向的节点
        2、将头节点所指向节点中的链接域1（pre）指向node
        3、将新节点设置为头节点
        :param item:
        :return:
        """
        node = Node(item)
        if self.__head is not None:
            node.next = self.__head
            self.__head.prev = node
        self.__head = node

    def append(self, item):
        pass
