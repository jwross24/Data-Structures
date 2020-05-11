class LinkedList:
    def __init__(self, nodes=None):
        '''
        Initialize the linked list, with optional input data.
        '''
        self.head = None
        self.tail = None
        if nodes:
            node = Node(value=nodes.pop(0))
            self.head = node
            self.tail = node
            for elem in nodes:
                node.next = Node(value=elem)
                node = node.next
                self.tail = node

    def __str__(self):
        '''
        String representation of the linked list.
        '''
        node = self.head
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(map(str, nodes))

    def __iter__(self):
        '''
        Pythonic traversal through a linked list.
        '''
        node = self.head
        while node:
            yield node
            node = node.next

    def add_to_tail(self, value):
        node = Node(value=value)
        if not self.head:
            self.head = node
            self.tail = node
            return None
        self.tail.next = node
        self.tail = self.tail.next

    def contains(self, value):
        return any(value == node.value for node in self)

        """
        Longer way:

        for node in self:
            if node.value == value:
                return True
        return False
        """

    def add_to_head(self, value):
        node = Node(value=value)
        if not self.head:
            self.head = node
            self.tail = node
            return None
        self.head, self.head.next = node, self.head

    def remove_head(self):
        if not self.head:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            if not self.head:
                self.tail = self.head
            return value

    def get_max(self):
        if not self.head:
            return None
        max_ = self.head.value
        for node in self:
            if max_ < node.value:
                max_ = node.value
        return max_


class Node:
    def __init__(self, value):
        '''
        Initialize a node with a value.
        '''
        self.value = value
        self.next = None

    def __str__(self):
        '''
        String representation of a node.
        '''
        return str(self.value)
