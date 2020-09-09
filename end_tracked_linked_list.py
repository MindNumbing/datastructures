#!/usr/bin/python3

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    head = None
    tail = None

    def __init__(self, *args):
        for arg in args:
            new_node = Node(arg)

            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = self.tail.next

    def __repr__(self):
        output = 'LinkedList('
        currentNode = self.head
        output = output + currentNode.value
        while currentNode.next != None:
            currentNode = currentNode.next
            output = output + ", " + currentNode.value
        output = output + ')'
        return output

cats = LinkedList("frank", "ben", "steve", "nick")
print(cats)
