class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


if __name__ == '__main__':
    llist = LinkedList()
    print(llist)

    first_node = Node('a')
    llist.head = first_node
    print(llist)

    second_node = Node('b')
    third_node = Node('c')
    first_node.next = second_node
    second_node.next = third_node
    print(llist)
