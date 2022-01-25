# Linked list with Node/LinkedList classes

VOWELS = {'a', 'e', 'i', 'o', 'u'}
class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node {self.data}>"


class LinkedList(object):
    """Linked List using head and tail"""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"<Linked List head={self.head}>"

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


def only_vowels(llist):
    """ Return a new LinkedList object containing nodes with the strings from
    the original linked list that start with vowels."""

    new_llist = LinkedList()

    current = llist.head

    while current:
        if current.data[0] in VOWELS:
            new_llist.add_node(current.data)
        current = current.next

    return new_llist