#!/usr/bin/python
import unittest

from linkedlist import (
    StackSL,
    StackDL,
    StackCL,
    QueueSL,
    QueueDL,
    QueueCL,
)

stackTypes = [ StackSL, StackDL, StackCL ]
queueTypes = [ QueueSL, QueueDL, QueueCL ]

stackTests = []
def addToStackTests( test ):
    stackTests.append( test )
    return test

queueTests = []
def addToQueueTests( test ):
    queueTests.append( test )
    return test

class TestBST( unittest.TestCase ):
    @addToStackTests
    def basicStackTest( self, Stack ):
        s = Stack()
        self.assertEqual( s.list_values(), [] )
        s.insert( 1 )
        s.insert( 2 )
        s.insert( 3 )
        self.assertEqual( s.list_values(), [ 3, 2, 1 ] )
        self.assertEqual( s.pop(), 3 )
        self.assertEqual( s.list_values(), [ 2, 1 ] )
        self.assertEqual( s.pop(), 2 )
        self.assertEqual( s.list_values(), [ 1 ] )
        self.assertEqual( s.pop(), 1 )
        self.assertEqual( s.list_values(), [] )

    @addToQueueTests
    def basicQueueTest( self, Queue ):
        s = Queue()
        self.assertEqual( s.list_values(), [] )
        s.insert( 1 )
        s.insert( 2 )
        s.insert( 3 )
        self.assertEqual( s.list_values(), [ 3, 2, 1 ] )
        self.assertEqual( s.pop(), 1 )
        self.assertEqual( s.list_values(), [ 3, 2 ] )
        self.assertEqual( s.pop(), 2 )
        self.assertEqual( s.list_values(), [ 3 ] )
        self.assertEqual( s.pop(), 3 )
        self.assertEqual( s.list_values(), [] )

    def testStackTypes( self ):
        for stackType in stackTypes:
#             print "testing {}".format( stackType.__name__ )
            for test in stackTests:
                test( self, stackType )

    def testQueueTypes( self ):
        for queueType in queueTypes:
#             print "testing {}".format( queueType.__name__ )
            for test in queueTests:
                test( self, queueType )

if __name__ == "__main__":
    unittest.main()
