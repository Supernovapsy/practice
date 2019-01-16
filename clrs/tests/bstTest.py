#!/usr/bin/python
import unittest

from bst import (
    Node,
    BST,
)

class TestBST( unittest.TestCase ):
    def setUp( self ):
        root = Node( 4 )
        self.bst = BST( root )
        root.insert_left( 2 )
        root.insert_right( 6 )
        root.left.insert_left( 1 )
        root.left.insert_right( 3 )
        root.right.insert_left( 5 )
        root.right.insert_right( 7 )
        self.verifyBST( self.bst )
        self.in_order = range( 1, 8 )
        self.reverse_order = list( reversed( self.in_order ) )

    def testMinMax( self ):
        self.assertEqual( self.bst.root.min().v, 1 )
        self.assertEqual( self.bst.root.max().v, 7 )

    def testSuccessor( self ):
        node = self.bst.min()

        inorder = list()
        while node:
            inorder.append( node.v )
            node = node.successor()

        self.assertEqual( inorder, self.in_order )

    def testPredecessor( self ):
        node = self.bst.max()

        reverse_order = list()
        while node:
            reverse_order.append( node.v )
            node = node.predecessor()

        self.assertEqual( reverse_order, self.reverse_order )

    def testInOrder( self ):
        self.assertEqual( self.bst.inorder(), self.in_order )

    def verifyBST( self, subtree ):
        inorder = subtree.inorder()
        self.assertEqual( inorder, sorted( inorder ) )

    def testOutOrder( self ):
        self.assertEqual( self.bst.outorder(), self.reverse_order )

    def testPreOrder( self ):
        self.assertEqual( self.bst.preorder(), [ 4, 2, 1, 3, 6, 5, 7 ] )

    def testLevelOrder( self ):
        self.assertEqual( self.bst.levelorder(), [ 4, 2, 6, 1, 3, 5, 7 ] )

    def testInsert( self ):
        for v in ( 0, 2.2, 6 ):
            self.bst.insert( v )
            self.assertIsNotNone( self.bst.find( v ) )
            self.verifyBST( self.bst )

    def testDelete( self ):
        for v in ( 1, 6, 4, 2, 7, 5, 3 ):
            self.bst.delete( v )
            self.assertIsNone( self.bst.find( v ) )
            self.verifyBST( self.bst )

if __name__ == "__main__":
    unittest.main()
