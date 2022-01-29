"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def get_num_children(self):
        """Get number of children.

        For example::

            >>> a = Node("A", [Node("B"), Node("C")])
            >>> a.get_num_children()
            2
        """

        return len(self.children)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def get_nodes(self, data):
        """ Return a list of nodes that contain the given data, in hierarchical order."""

        # Complete this function
        # heirarchical order => Breadth First Search idea
        # BFS means we should think about a queue data structure
        # Queue => add new nodes to end, remove nodes at index 0

        occurences = []
        to_visit = [self.root]
        print("\n We just created a list, to_visit: ", to_visit)

        while to_visit:
            node = to_visit.pop(0)
            print("\n We're in the while loop, node: ", node)

            if node.data == data:
                occurences.append(node)
                print("\n We're in the if statement and just appended to occurences, occurences: ", occurences)

            to_visit.extend(node.children)

        print("\n We're right before the return, occurences: ", occurences)
        return occurences


if __name__ == "__main__":
    b1 = Node("B")
    b2 = Node("B")
    b3 = Node("B")
    e = Node("E", [b3])
    c = Node("C", [ b1, e])
    a = Node("A", [b2, c])
    tree = Tree(a)

    #       a
    #      / \
    #     b2  c
    #        / \
    #       b1  e
    #            \
    #             b3

    print("\n tree.get_nodes('B') == [b2, b1, b3]: ", tree.get_nodes("B") == [b2, b1, b3])

    print("\n")
    print("*"* 30)

    print("\n tree.get_nodes('L') == []: ", tree.get_nodes("L") == [])
