class NodeSL( object ):
    def __init__( self, v ):
        self.v = v
        self.next = None

class NodeDL( object ):
    def __init__( self, v ):
        self.v = v
        self.next = None
        self.prev = None

class SLL( object ):
    def __init__( self ):
        self.head = None
        self.tail = None

    def first_node( self ):
        return self.head

    def insert_head( self, v ):
        node = NodeSL( v )
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def insert_tail( self, v ):
        node = NodeSL( v )
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = self.head = node

    def pop_head( self ):
        if not self.head:
            return None

        node = self.head
        self.head = node.next
        if self.head is None: # deleting last element.
            self.tail = None
        return node

    def pop_tail( self ):
        if not self.tail:
            return None
        elif self.tail is self.head:
            node = self.head
            self.head = self.tail = None
            return node

        node = self.head
        while node.next is not self.tail:
            node = node.next
        assert node, "We should be able to reach tail from head."

        # node.next is self.tail
        last_node = self.tail
        self.tail = node
        self.tail.next = None
        return last_node

class DLL( object ):
    def __init__( self ):
        self.head = None
        self.tail = None

    def first_node( self ):
        return self.head

    def insert_head( self, v ):
        node = NodeDL( v )
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def insert_tail( self, v ):
        node = NodeDL( v )
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def pop_head( self ):
        if not self.head:
            return None
        elif self.head is self.tail:
            node = self.head
            self.head = self.tail = None
            return node

        node = self.head
        self.head = self.head.next
        self.head.prev = None
        return node

    def pop_tail( self ):
        if not self.tail:
            return None
        elif self.tail is self.head:
            node = self.tail
            self.head = self.tail = None
            return node

        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return node

class CLL( object ):
    """CLLs can be either singly linked or doubly linked

    Here we use singly linked for simplicity.
    """
    def __init__( self ):
        self.tail = None

    def first_node( self ):
        return self.tail.next if self.tail else None

    def insert_head( self, v ):
        node = NodeSL( v )
        if not self.tail:
            self.tail = node
            self.tail.next = self.tail
        else:
            node.next = self.tail.next
            self.tail.next = node

    def insert_tail( self, v ):
        self.insert_head( v )
        self.tail = self.tail.next

    def pop_helper( self, pop_head=True ):
        assert isinstance( pop_head, bool )
        if not self.tail:
            return None
        elif self.tail.next is self.tail:
            node = self.tail
            self.tail = None
            return node
        else:
            # popping tail, reduce to the problem of popping head.
            if not pop_head:
                new_tail = self.tail
                while new_tail.next is not self.tail:
                    new_tail = new_tail.next
                self.tail = new_tail

            node = self.tail.next
            self.tail.next = node.next
            return node

    def pop_head( self ):
        return self.pop_helper( pop_head=True )

    def pop_tail( self ):
        return self.pop_helper( pop_head=False )

def stackClass( LinkedList ):
    class Stack( object ):
        def __init__( self ):
            self.list = LinkedList()

        def list_values( self ):
            """Prints elements in order"""
            first = self.list.first_node()
            if first:
                ret = [ first.v ]
            else:
                return []

            node = first.next
            while node and node is not first:
                ret.append( node.v )
                node = node.next
            return ret

        def insert( self, v ):
            self.list.insert_head( v )

        def pop( self ):
            return self.list.pop_head().v
    return Stack

def queueClass( LinkedList ):
    class Queue( object ):
        def __init__( self ):
            self.list = LinkedList()

        def list_values( self ):
            """Prints elements in order"""
            first = self.list.first_node()
            if first:
                ret = [ first.v ]
            else:
                return []

            node = first.next
            while node and node is not first:
                ret.append( node.v )
                node = node.next
            return ret

        def insert( self, v ):
            self.list.insert_head( v )

        def pop( self ):
            return self.list.pop_tail().v
    return Queue

StackSL = stackClass( SLL )
StackDL = stackClass( DLL )
StackCL = stackClass( CLL )
QueueSL = queueClass( SLL )
QueueDL = queueClass( DLL )
QueueCL = queueClass( CLL )
