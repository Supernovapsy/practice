#!/usr/bin/python
import unittest

def bin_search( lst, x, i=None, j=None ):
    i = i or 0
    j = j or len( lst )
    if j - i == 1:
        return i if lst[ i ] == x else -1
    m = ( i + j ) / 2
    ret = bin_search( lst, x, i, m )
    if ret != -1:
        return ret
    return bin_search( lst, x, m, j )

def bin_search2( lst, n, i=None, j=None ):
    i = i or 0
    j = j or len( lst )

    length = j - i
    if length == 0:
        return None
    elif length == 1:
        return i if n == lst[ i ] else None

    # recursive case: length >= 2
    mid = ( j + i ) / 2
    mid_v = lst[ mid ]
    if mid_v == n:
        return mid
    elif mid_v > n:
        return bin_search2( lst, n, i, mid )
    else:
        return bin_search2( lst, n, mid + 1, j )

def bin_search_iterative( lst, n ):
    i, j = 0, len( lst )
    while i != j:
        mid = ( i + j ) / 2
        if lst[ mid ] == n:
            return mid
        elif lst[ mid ] < n:
            i = mid + 1
        else:
            j = mid
    return None

class TestAlgos( unittest.TestCase ):
    def testBinSearch( self ):
        self.assertEqual( bin_search_iterative( [ 2, 4, 6, 8, 12 ], 6 ), 2 )
        self.assertEqual( bin_search_iterative( [ 2, 4, 6, 8, 12 ], 12 ), 4 )
        self.assertEqual( bin_search_iterative( [ 2, 4, 6, 8, 12 ], 2 ), 0 )
        self.assertEqual( bin_search_iterative( [ 2, 4, 6, 8, 12 ], 3 ), None )

if __name__ == '__main__':
    unittest.main()
