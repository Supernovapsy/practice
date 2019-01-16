# all sort functions

# input: list
# output: list containing sorted elements (can modify old list).

sortFns = []

def getAllFns():
    return sortFns[ : ]

def addSortFn( fn ):
    """Decorator for sortFns."""
    sortFns.append( fn )
    return fn

@addSortFn
def insertion_sort( lst ):
    for i in xrange( 1, len( lst ) ):
        ele = lst[ i ]
        j = i - 1
        while lst[ j ] > ele and j >= 0:
            lst[ j + 1 ] = lst[ j ]
            j -= 1
        lst[ j + 1 ] = ele
    return lst

def merge_sort_aux( lst, i, j ):
    """Must not change lst, and return a new list object"""
    if j - i == 1:
        return [ lst[ i ] ]
    m = ( i + j ) / 2
    left = merge_sort_aux( lst, i, m )
    right = merge_sort_aux( lst, m, j )
    return merge( left, right )

def merge( left, right ):
    lst = []
    l = r = 0
    while l != len( left ) and r != len( right ):
        if left[ l ] <= right[ r ]:
            lst.append( left[ l ] )
            l += 1
        else:
            lst.append( right[ r ] )
            r += 1
    if l != len( left ):
        while l != len( left ):
            lst.append( left[ l ] )
            l += 1
    else:
        while r != len( right ):
            lst.append( right[ r ] )
            r += 1
    return lst

@addSortFn
def merge_sort( lst ):
    return merge_sort_aux( lst, 0, len( lst ) )

def quick_sort_aux( lst, i, j ):
    if j - i <= 1:
        return

    pivot = lst[ i ]
    less_count = 0
    for k in xrange( i, j ):
        if lst[ k ] < pivot:
            less_count += 1
    k = i + less_count # position of pivot element.

    lst[ k ], lst[ i ] = lst[ i ], lst[ k ]
    a, b = i, k + 1 # starting indices on the left and right partitions.
    while True:
        while a != k and lst[ a ] < pivot:
            a += 1
        while b != j and lst[ b ] >= pivot:
            b += 1
        if a == k or b == j:
            assert a == k and b == j
            break
        lst[ a ], lst[ b ] = lst[ b ], lst[ a ]
        a += 1
        b += 1

    quick_sort_aux( lst, i, k )
    quick_sort_aux( lst, k + 1, j )

@addSortFn
def quick_sort( lst ):
    quick_sort_aux( lst, 0, len( lst ) )
    return lst

# heap:
#      0
#    /   \
#   1     2
#  / \   / \
# 3   4 5   6
#
# left = 2*i + 1
# right = 2*i + 2

def left( i ):
    return 2 * i + 1

def right( i ):
    return 2 * i + 2

def parent( i ):
    return ( i - 1 ) / 2

def heap_insert( lst, e ):
    lst.append( e )
    i = len( lst ) - 1
    p = parent( i )
    while i != 0 and e > lst[ p ]:
        lst[ p ], lst[ i ] = lst[ i ], lst[ p ]
        i = p
        p = parent( i )

def max_heapify( lst, i ):
    """i is the root of the sub-tree"""
    while True:
        l, r = left( i ), right( i )
        if l >= len( lst ):
            break
        elif l == len( lst ) - 1:
            m = l
        else:
            m = l if lst[ l ] >= lst[ r ] else r

        if lst[ m ] > lst[ i ]:
            lst[ i ], lst[ m ] = lst[ m ], lst[ i ]
            i = m
        else:
            break

def heap_pop( lst ):
    if not len( lst ):
        return Exception( "lst is empty" )
    elif len( lst ) == 1:
        return lst.pop()

    e = lst[ 0 ]
    lst[ 0 ] = lst.pop()

    max_heapify( lst, 0 )
    return e

def heap_delete( lst, i ):
    if i == len( lst ) - 1:
        return lst.pop()

    e = lst[ i ]
    lst[ i ] = lst.pop()
    max_heapify( lst, i )
    return e

@addSortFn
def heap_sort( lst ):
    for i in xrange( parent( len( lst ) - 1 ), -1, -1 ):
        max_heapify( lst, i )

    ret = list()
    while lst:
        ret.append( heap_pop( lst ) )

    return list( reversed( ret ) )
