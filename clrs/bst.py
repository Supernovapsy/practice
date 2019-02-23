class Node( object ):
    def __init__( self, v ):
        self.v = v
        self.left = None
        self.right = None
        self.parent = None

    def insert_left( self, v ):
        self.left = Node( v )
        self.left.parent = self

    def insert_right( self, v ):
        self.right = Node( v )
        self.right.parent = self

    def min( self ):
        node = self
        while node.left:
            node = node.left
        return node

    def max( self ):
        node = self
        while node.right:
            node = node.right
        return node

    def predecessor( self ):
        if self.left:
            return self.left.max()
        node = self
        while node.parent:
            if node.parent.right is node:
                return node.parent
            assert node.parent.left is node
            node = node.parent
        return None # it's the minimum element

    def successor( self ):
        if self.right:
            return self.right.min()
        node = self
        while node.parent:
            if node.parent.left is node:
                return node.parent
            assert node.parent.right is node
            node = node.parent
        return None # It's the maximum element

def transplant( t, u, v ):
    """transplant v onto u"""
    assert u

    if not u.parent:
        assert t.root is u
        t.root = v
    elif u.parent.left is u:
        u.parent.left = v
    elif u.parent.right is u:
        u.parent.right = v

    if v:
        v.parent = u.parent

class BST( object ):
    def __init__( self, root ):
        self.root = root

    def min( self ):
        if not self.root:
            return None
        return self.root.min()

    def max( self ):
        if not self.root:
            return None
        return self.root.max()

    def find( self, v ):
        """Returns node containing v. None if not found."""
        n = self.root
        while n:
            if v == n.v:
                return n
            elif v < n.v:
                n = n.left
            else:
                n = n.right
        return None

    def insert( self, v ):
        if not self.root:
            self.root = Node( v )
            return

        node = self.root
        while True:
            if v <= node.v:
                if not node.left:
                    node.insert_left( v )
                    return
                else:
                    node = node.left
            else:
                if not node.right:
                    node.insert_right( v )
                    return
                else:
                    node = node.right
            assert node is not self.root, "cycle in BST!"

    def delete( self, v ):
        """Deletes node and returns it. raises KeyError if not found."""
        node = self.find( v )
        if not node:
            raise KeyError( "Deleting non-existent element" )

        if not node.left:
            transplant( self, node, node.right )
        elif not node.right:
            transplant( self, node, node.left )
        else:
            # both childs are present.
            y = node.right
            z = y.min()
            if z is not y:
                transplant( self, z, z.right )
                z.right = y
                y.parent = z
            transplant( self, node, z )
            z.left = node.left
            z.left.parent = z

    def inorder( self, node=None ):
        """Just like preorder, the iterative solution, aside from bigger code
        size, is superior in constant factor for time and space.

        NOTE: There is a shorter solution than this which exploits all cases of
        what happens to a node on Wikipedia; however, it's not something I
        expect myself to come up during an interview.

        This is implemented for outorder below. Note the method by which this
        two-classes of queue items is solved is by changing the algorithm to
        only operate on one type of queue item, but process them in two
        different ways depending on its properties - in this case whether the
        current subtree rooted at the specified node is empty or not.
        """
        node = node or self.root

        q = []
        inorder_list = [] # Return value

        while q or node:
            if node:
                q.append( node )
                node = node.left
            else:
                node = q.pop()
                # visit
                inorder_list.append( node.v )
                node = node.right

        return inorder_list

    def preorder( self, node=None ):
        """pre-order gives a topological ordering of the nodes in a tree.

        Assuming we have a balanced tree, both the iterative and recurisve
        solutions use theta(n) time and theta(h) space => we should almost
        always use iterative solution to save on the constant factor cost of
        function calling.
        """
        node = node or self.root

        q = [ node ] # stack
        preorder_list = [] # return value

        while q:
            node = q.pop()
            if not node:
                continue
            preorder_list.append( node.v )
            q.append( node.right )
            q.append( node.left )

        return preorder_list

    def outorder( self, node=None ):
        """Reverse order"""
        node = node or self.root

        q = []
        outorder_list = [] # return value
        while q or node:
            if node:
                q.append( node )
                node = node.right
            else:
                node = q.pop()
                outorder_list.append( node.v )
                node = node.left

        return outorder_list

    def levelorder( self, node=None ):
        """Same as canonical BFS"""
        node = node or self.root

        frontier = [ node ]
        next_frontier = []
        levelorder_list = [] # return value
        while frontier:
            for node in frontier:
                if not node:
                    continue
                levelorder_list.append( node.v )
                next_frontier.append( node.left )
                next_frontier.append( node.right )
            frontier = next_frontier
            next_frontier = []
        return levelorder_list

# TODO when have time
class AvlTree( BST ):
    pass
