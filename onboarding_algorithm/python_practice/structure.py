class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)

    def remove(self, val):
        node = self.head
        if node.val == val:
            self.head.next = node.next
            del (node)
            return
        while node.next:
            prev = self.head
            curr = prev.next
            if curr.val == val:
                prev.next = curr.next
                del (curr)
                return

    def print(self):
        node = self.head
        while node:
            print(node.val, end=' ')
            node = node.next

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if not self.top:
            return None
        
        node = self.top
        self.top = self.top.next

        return node.val
    
class Queue:
    def __init__(self):
        self.front = None
      
    def is_empty(self):
        return self.front is None
    
    def push(self, val):
        if not self.front:
          self.front = Node(val, None)
          return
          
        node = self.front
        while node.next:
            node = node.next
        node.next = Node(val, None)

    def pop(self):
        if not self.front:
            return None
        
        node = self.front
        self.front = self.front.next

        return node.val