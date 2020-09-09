#!/usr/bin/python3

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    head = None

    def push(self, value):
        new_node = Node(value)

        if self.head:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            return
        self.head = new_node

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        return self.head.value

    def __repr__(self):
        output = 'Stack('
        current_node = self.head
        output = output + current_node.value
        while current_node.next != None:
            current_node = current_node.next
            output = output + ', ' + current_node.value
        output = output + ')'
        return output

stack = Stack()
stack.push('Marlin')
stack.push('Boscow')
print(stack.peek())
print(stack.pop())
stack.push('Shadow')
print(stack)