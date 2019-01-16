#!/usr/bin/python
import unittest
from random import randrange

import sort
from sort import (
    heap_insert,
    max_heapify,
    heap_pop,
    heap_delete,
    parent,
)

tests = []
def addToTests( test ):
    tests.append( test )
    return test

class TestSort( unittest.TestCase ):
    @addToTests
    def basic( self, sort_fn ):
        lst = [ 4, 2, 1, 3 ]
        lst_in = lst[ : ]
        lst.sort()
        self.assertEqual( lst, sort_fn( lst_in ) )

    @addToTests
    def basic2( self, sort_fn ):
        lst = [ 7, 4, 2, 9 ]
        lst_in = lst[ : ]
        lst.sort()
        self.assertEqual( lst, sort_fn( lst_in ) )

    @addToTests
    def basic3( self, sort_fn ):
        lst = [ 1234, 3214, 2314, 3214, 4213 ]
        lst_in = lst[ : ]
        lst.sort()
        self.assertEqual( lst, sort_fn( lst_in ) )

    @addToTests
    def longRand( self, sort_fn ):
        n = 1000
        lst = [ randrange( 0, 65536 ) for i in xrange( n ) ]
        lst_in = lst[ : ]
        lst.sort()
        self.assertEqual( lst, sort_fn( lst_in ) )

    def testAll( self ):
        for sortFn in sort.getAllFns():
            print "testing {}".format( sortFn.__name__ )
            for test in tests:
                test( self, sortFn )

    def verifyHeap( self, lst ):
        for i in xrange( 1, len( lst ) ):
            self.assertLessEqual( lst[ i ], lst[ parent( i ) ],
                                  "i = {}, p = {}".format( i, parent( i ) ) )

    def testHeapInsert( self ):
        lst = [ 6, 4, 2, 1, 3 ]
        lstc = lst[ : ]
        self.verifyHeap( lst )
        heap_insert( lst, 7 )
        lstc.append( 7 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )
        heap_insert( lst, 5 )
        lstc.append( 5 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )
        heap_insert( lst, 3 )
        lstc.append( 3 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )

    def testHeapPop( self ):
        lst = [ 6, 4, 2, 1, 3 ]
        lstc = set( lst )
        self.verifyHeap( lst )
        self.assertEqual( heap_pop( lst ), 6 )
        lstc.discard( 6 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )
        self.assertEqual( heap_pop( lst ), 4 )
        lstc.discard( 4 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )
        self.assertEqual( heap_pop( lst ), 3 )
        lstc.discard( 3 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )

    def testHeapDelete( self ):
        lst = [ 6, 4, 2, 1, 3 ]
        lstc = set( lst )
        self.verifyHeap( lst )
        lstc.discard( lst[ len( lst ) - 1 ] )
        heap_delete( lst, len( lst ) - 1 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )
        lstc.discard( lst[ 1 ] )
        heap_delete( lst, 1 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )
        lstc.discard( lst[ 0 ] )
        heap_delete( lst, 0 )
        self.verifyHeap( lst )
        self.assertItemsEqual( lst, lstc )

if __name__ == '__main__':
    unittest.main()
