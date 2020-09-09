#!/usr/bin/python3

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    head = None

    def __init__(self, *args):
        for arg in args:
            new_node = Node(arg)
            if self.head:
                currentNode = self.head
                while currentNode.next:
                    currentNode = currentNode.next
                currentNode.next = new_node
                return
            else:
                self.head = new_node


    def __repr__(self):
        if self.head:
            output = 'LinkedList('
            currentNode = self.head
            output = output + currentNode.value
            while currentNode.next != None:
                currentNode = currentNode.next
                output = output + ", " + currentNode.value
            output = output + ')'
            return output

cats = LinkedList("frank", "ben")
print(cats)