class LinkedList:
    def __init__(self, nodes=None):
        '''
        Initialize the linked list, with optional input data.
        '''
        self.head = None
        if nodes:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(value=elem)
                node = node.next

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
        return " -> ".join(nodes)

    def __iter__(self):
        '''
        Pythonic traversal through a linked list.
        '''
        node = self.head
        while node:
            yield node
            node = node.next


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
        return self.value


if __name__ == '__main__':
    llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
    print(llist)

    for node in llist:
        print(node)
