"""

https://realpython.com/linked-lists-python/#implementing-your-own-linked-list
"""


class Node:
    """
    Class to represent each node of the list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """
        To have a more helpful representation of the objects
        :return: our data
        """
        return self.data


class LinkedList:
    """
    Class to represent linked list.

    """
    def __init__(self):
        # the head of the list, information where the list start
        self.head = None

    def __repr__(self):
        """
        To have a more helpful representation of the objects
        :return: our data
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


link_list = LinkedList()
print(link_list)

first_node = Node("b")
print(first_node)
link_list.head = first_node
print(link_list)

second_node = Node("g")
third_node = Node("z")
first_node.next = second_node
second_node.next = third_node
print(link_list)