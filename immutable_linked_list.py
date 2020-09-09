#!/usr/bin/python3

from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: Optional[str] = None
    next: Optional[str] = None

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def push(self, value):
        if not self.value:
            self.value = value
            return
        current_node = self
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)

    def pop(self):
        if not self.value: return
        if not self.next:
            return self.value, Node()
        return self.value, self.next

    def peek(self):
        if not self.value: return
        return self.value

    def __repr__(self, out=""):
        if self.value == None: return
        out = out + self.value + " "
        if self.next: out = self.next.__repr__(out)
        return out

cats = Node()
cats.push("Ada")
cats.push("Sheba")
cats.push("Wirl")

print(cats)

print("")

kitty = cats.peek()

print(kitty)

print("")

kitty, cats = cats.pop()
print(kitty)
print(cats)
