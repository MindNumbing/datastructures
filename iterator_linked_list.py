#!/usr/bin/python3

from dataclasses import dataclass
from typing import Optional, Tuple

class LinkedListIterator:

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current.next == None:
            raise StopIteration
        else:
            value = self.current.value
            self.current = self.current.next
            return value

@dataclass(frozen=True)
class Node:
    value: Optional[str] = None
    next: Optional["Node"] = None

    def push(self, value: str) -> "Node":
        # (ada).push("sheba") -- self = ada, value = sheba
        return Node(value, self)

    def pop(self) -> Tuple[str, Optional["Node"]]:
        if not self.value: raise Exception("No kitties available :(")
        return self.value, self.next

    def peek(self) -> Optional[str]:
        return self.value

    def __repr__(self) -> str:
        return str([kitty for kitty in self])

    def reverse(self, node: Optional["Node"] = None) -> "Node":
        if not node: node = Node()
        if self.next:
            new_node = self.next.reverse(Node(self.value, node))
            return new_node
        return node

    def contains(self, name: str) -> bool:
        if name in self:
            return True
        return False

    def remove(self, name: str) -> "Node":
        if not self.contains(name):
            print("Didn't find name")
            return self

        new_node = Node()
        for node in self:
            if node != name:
                new_node = new_node.push(node)
            else:
                print("Skipping name")
        return new_node

    def __iter__(self):
      return LinkedListIterator(self)

empty_list = Node()
list1 = empty_list.push("Ada")
print(list1)
list2 = list1.push("Sheba")
print(list2)
list3 = list2.push("Wirl")
print(list3)

list3.peek()

kitty, cats = list3.pop()
print(kitty)
print(type(cats))
print(cats)

print("")
new_list = list3.reverse()
print("Original list: ", list3)
print("Reversed list: ", new_list)

empty_list = Node()
list1 = empty_list.push("Alex")
list2 = list1.push("Max")
list3 = list2.push("Katey")

for kitty in list3:
    print(kitty)

print("")
print(list3.contains("Alex"))

print("")
nodelist = list3.remove("Agatha")
print(nodelist)

print("")
nodelist = list3.remove("Max")
print(nodelist)