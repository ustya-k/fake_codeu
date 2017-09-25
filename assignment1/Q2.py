# -*- coding: utf-8 -*-


class Node():
    """
    A minimal component of a linked list.
    """

    def __init__(self, data):
        """
        Initializes a minimal component of a linked list,
        which collects a given data and a link to the next
        element of the linked list.

        Args:
            * data: what needs to be added in the linked list.
        """

        self.data = data
        self.next_node = None


class LinkedList():
    """
    A linked list data structure itself.
    """

    def __init__(self):
        """
        Initializes a linked list, creates a None head of the list.
        """

        self.head = None

    def add_item(self, data):
        """
        Adds a new item to the linked list.

        Args:
            * data: what needs to be added in the linked list.
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search_for_kth_element(self, k):
        """
        Searches for the kth to last element of the linked list.

        Args:
            * k (int): a needed position.
        Returns:
            * needed_element:the kth to last element of the
            linked list.
        """

        current_node = self.head
        i = 0

        while i <= k - 1:
            current_node = current_node.next_node
            i += 1

        needed_element = current_node.data

        return needed_element


if __name__ == '__main__':
    main()
