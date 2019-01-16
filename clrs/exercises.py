#!/usr/bin/python
import unittest
from sort import merge_sort
from algos import bin_search

def pair_sum_exists( lst, x ):
    lst = merge_sort( lst )
    for i in xrange( len( lst ) - 1 ):
        target = x - lst[ i ]
        index = bin_search( lst, target, i + 1, len( lst ) )
        if index != -1:
            return True
    return False

def placeholder( lst, x ):
    raise NotImplementedError()

class TestExercises( unittest.TestCase ):
    def test2_3_7( self ):
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 6 ), True )
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 12 ), True )
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 2 ), False )
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 3 ), False )
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 14 ), True )
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 20 ), True )
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 0 ), False )
        self.assertEqual( pair_sum_exists( [ 2, 4, 6, 8, 12 ], 17 ), False )

if __name__ == '__main__':
    unittest.main()
