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

# Using dictionary gives us O(1) instead of O(n) for list
VOWELS = {'a', 'e', 'i', 'o', 'u'}

def only_vowels(llist):
    """ Return a new LinkedList object containing nodes with the strings from
    the original linked list that start with vowels."""

    new_llist = LinkedList()
    print("\n We just created an empty linked list, new_llist: ", new_llist)

    current = llist.head

    while current:
        print("\n We're in the while loop, current: ", current)
        if current.data[0] in VOWELS:
            new_llist.add_node(current.data)
            print("\n We're in the if statement and just appended to new_llist, new_llist: ", new_llist)
        current = current.next

    print("\n We're right before the return, new_llist: ", new_llist)
    return new_llist



if __name__ == "__main__":
    llist = LinkedList()
    llist.add_node("cherry")
    llist.add_node("berry")
    llist.add_node("apple")
    only_vowels_llist = only_vowels(llist)
    # Iterate over new linked list we just created
    # from calling the "only_vowels" function
    current = only_vowels_llist.head
    while current:
        print("\n We're outside the only_vowels function and iterating over the new_llist we returned, node: ", current)
        current = current.next

    print("\n")
    print("*"* 30)

    llist = LinkedList()
    llist.add_node("cherry")
    llist.add_node("avocado")
    llist.add_node("berry")
    llist.add_node("apple")
    only_vowels_llist = only_vowels(llist)
    # Iterate over new linked list we just created
    # from calling the "only_vowels" function
    current = only_vowels_llist.head
    while current:
        print("\n We're outside the only_vowels function and iterating over the new_llist we returned, node: ", current)
        current = current.next

    print("\n")
    print("*"* 30)

    llist = LinkedList()
    llist.add_node("cherry")
    llist.add_node("strawberry")
    llist.add_node("berry")
    llist.add_node("watermelon")
    only_vowels_llist = only_vowels(llist)
    # Iterate over new linked list we just created
    # from calling the "only_vowels" function
    current = only_vowels_llist.head
    while current:
        print("\n We're outside the only_vowels function and iterating over the new_llist we returned, node: ", current)
        current = current.next