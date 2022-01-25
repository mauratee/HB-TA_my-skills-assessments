"""Tests for tree.py and linkedlist.py"""

from tree import Tree, Node as TreeNode
from linkedlist import LinkedList, only_vowels

# Tests for only_vowels


def test_only_vowels_single_vowel_word():
    llist = LinkedList()
    llist.add_node("cherry")
    llist.add_node("berry")
    llist.add_node("apple")
    only_vowels_llist = only_vowels(llist)
    assert only_vowels_llist.head.data == "apple"
    assert only_vowels_llist.tail.data == "apple"

def test_only_vowels_multiple_vowel_words():
    llist = LinkedList()
    llist.add_node("cherry")
    llist.add_node("avocado")
    llist.add_node("berry")
    llist.add_node("apple")
    only_vowels_llist = only_vowels(llist)
    assert only_vowels_llist.head.data == "avocado"
    assert only_vowels_llist.tail.data == "apple"

def test_only_vowels_no_vowels():
    llist = LinkedList()
    llist.add_node("cherry")
    llist.add_node("strawberry")
    llist.add_node("berry")
    llist.add_node("watermelon")
    only_vowels_llist = only_vowels(llist)
    assert only_vowels_llist.head is None
    assert only_vowels_llist.tail is None

def test_get_nodes_with_matching_nodes():

    b1 = TreeNode("B")
    b2 = TreeNode("B")
    b3= TreeNode("B")
    e = TreeNode("E", [b3])
    c = TreeNode("C", [ b1, e])
    a = TreeNode("A", [b2, c])
    tree = Tree(a)
    assert tree.get_nodes("B") == [b2, b1, b3]

def test_get_nodes_empty():

    b1 = TreeNode("B")
    b2 = TreeNode("B")
    b3= TreeNode("B")
    e = TreeNode("E", [b3])
    c = TreeNode("C", [ b1, e])
    a = TreeNode("A", [b2, c])
    tree = Tree(a)
    assert tree.get_nodes("L") == []