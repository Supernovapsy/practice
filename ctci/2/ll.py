import sys
import random

class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# singly
class linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def prt(self):
        it = self.head
        while it:
            sys.stdout.write(str(it.value))
            if it != self.tail:
                sys.stdout.write(' -> ')
            else:
                sys.stdout.write('\n')
            it = it.next

    def insert(self, value):
        newNode = node(value)
        if self.tail:
            self.tail.next = newNode
            self.tail = self.tail.next
        else:
            # This means that the head also does not exist.
            self.head = self.tail = newNode

    def delete_key(self, head, value):
        if head is None:
            return head
        elif self.head == head and head.value == value:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return self.head
        else:
            it = head
            while it.next is not None:
                if it.next.value == value:
                    if it.next == self.tail:
                        self.tail = it
                    it.next = it.next.next
                    return it.next
                it = it.next
        return None

    def delete(self, head, node):
        """Assumes that head is part of the called linked list."""
        if head is None:
            return head
        elif self.head == head and head == node:
            # If deleting the head of the ll.
            if self.tail == node:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return self.head
        else:
            it = head
            while it.next is not None:
                if it.next == node:
                    if it.next == self.tail:
                        self.tail = it
                    it.next = it.next.next
                    return it.next
                it = it.next
        return None

egll = linked_list()
for i in range(20):
    ele = random.randrange(10)
    egll.insert(ele)
