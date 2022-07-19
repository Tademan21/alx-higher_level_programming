#!/usr/bin/python3
"""Singly Linked Lists module.
This module contains methods about the creation and hendling of
SinglyLinkedList and Node objects.
"""


class Node():
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Sets the necessary attributes for the Node object.
        Args:
            data (int): the value of the node
            next_node (Node): the next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data value of a node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get or set the next node of the current node."""
        return self.__next_node

    @next_node.setter

