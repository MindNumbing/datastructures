#!/usr/bin/python3

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Cats():

    head = None
    tail = None
    node_count = 0

    def add(self, value):
        self.node_count = self.node_count + 1
    
        new_node = Node(value)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node

    def remove(self):
        if self.head:
            self.node_count = self.node_count - 1

            old_head = self.head
            self.head = old_head.next
            return old_head.value
        raise "No head"

    def count(self):
        return self.node_count

cats = Cats()
print(cats.count())
cats.add("Tidbit")
print(cats.count())
cats.add("Marmalade")
print(cats.count())
cats.add("Splinter")
print(cats.count())
print(cats.remove())
print(cats.count())
