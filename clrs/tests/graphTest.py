#!/usr/bin/python
import unittest
import numpy as np

from graph import (
    VisitRecord,
    construct_path,
    iteredges,
    bfs,
    dfs,
    find_scc,
    sort_by_dfs_reverse_finish,
    has_cycle,
    bellman_ford,
    dijkstra,
    dag_shortest_path,
    mst_prim,
    mst_kruskal,
)

class TestGraph( unittest.TestCase ):
    # TODO: make this setUpClass
    def setUp( self ):
        self.nodes = 9

        # some strongly-connected components.
        self.adj = {
            0: [ 1, 6 ],
            1: [ 2 ],
            2: [ 0, 3, 6, 7 ],
            3: [ 5 ],
            4: [ 3 ],
            5: [ 4 ],
            6: [ 7, 8 ],
            7: [ 6 ],
            8: [ 4 ],
        }
        self.assertEqual( len( self.adj ), self.nodes )

        self.adjw = np.ones( ( self.nodes, self.nodes ) ) * np.inf
        self.adjw[0][1] = 0
        self.adjw[0][6] = 6
        self.adjw[1][2] = 2
        self.adjw[2][0] = 1
        self.adjw[2][3] = 2
        self.adjw[2][6] = -2
        self.adjw[2][7] = -5
        self.adjw[3][5] = 1
        self.adjw[4][3] = 1
        self.adjw[5][4] = 2
        self.adjw[6][7] = -2
        self.adjw[6][8] = 1
        self.adjw[7][6] = 2
        self.adjw[8][4] = -3

        # Positive weights version (required by dijkstra)
        self.adjwp = np.absolute( self.adjw )

        self.components = set( (
            frozenset( [ 0, 1, 2 ] ),
            frozenset( [ 3, 4, 5 ] ),
            frozenset( [ 6, 7 ] ),
            frozenset( [ 8 ] ),
        ) )

        # undirected version
        self.adj_ud = {
            0: [ 1, 2, 6 ],
            1: [ 0, 2, 6 ],
            2: [ 0, 1, 3, 6, 7 ],
            3: [ 2, 4, 5 ],
            4: [ 3, 5, 8 ],
            5: [ 3, 4 ],
            6: [ 0, 1, 2, 7, 8 ],
            7: [ 2, 6 ],
            8: [ 4, 6 ],
        }
        self.assertEqual( len( self.adj_ud ), self.nodes )
        # Handshaking lemma: sum of the degrees must be even.
        self.assertEqual(
            sum( map( len, self.adj_ud.values() ) ) % 2, 0 )

        self.adjw_ud = np.ones( ( self.nodes, self.nodes ) ) * np.inf
        self.adjw_ud[0][1] = 0
        self.adjw_ud[0][6] = 6
        self.adjw_ud[1][2] = 2
        self.adjw_ud[2][0] = 1
        self.adjw_ud[2][3] = 2
        self.adjw_ud[2][6] = -2
        self.adjw_ud[2][7] = -5
        self.adjw_ud[3][5] = 1
        self.adjw_ud[4][3] = 1
        self.adjw_ud[5][4] = 2
        self.adjw_ud[6][7] = -2
        self.adjw_ud[6][8] = 1
        self.adjw_ud[8][4] = -3
        for i in xrange( self.nodes ):
            for j in xrange( self.nodes ):
                if self.adjw_ud[ i ][ j ] != np.inf:
                    self.adjw_ud[ j ][ i ] = self.adjw_ud[ i ][ j ]

        # Some algorithms operate on dags.
        self.dag = {
            0: [ 1, 2, 3, 4 ],
            1: [ 6 ],
            2: [ 5 ],
            3: [ 2, 6, 7 ],
            4: [ 1, 3 ],
            5: [ 8 ],
            6: [ 7, 8 ],
            7: [ 8 ],
            8: [],
        }
        self.assertEqual( len( self.dag ), self.nodes )

        self.dagw = np.ones( ( self.nodes, self.nodes ) ) * np.inf
        self.dagw[0][1] = 1
        self.dagw[0][2] = 2
        self.dagw[0][3] = 2
        self.dagw[0][4] = 2
        self.dagw[1][6] = -5
        self.dagw[2][5] = 4
        self.dagw[3][2] = -1
        self.dagw[3][6] = 4
        self.dagw[3][7] = -7
        self.dagw[4][1] = 6
        self.dagw[4][3] = 3
        self.dagw[5][8] = 2
        self.dagw[6][7] = 3
        self.dagw[6][8] = 6
        self.dagw[7][8] = 8

        self.dag_levels = [
            set( [ 0 ] ),
            set( [ 1, 2, 3, 4 ] ),
            set( [ 5, 6, 7 ] ),
            set( [ 8 ] ),
        ]
        self.assertEqual( sum( map( len, self.dag_levels ) ),
                          self.nodes )

    def verifyTopologicalOrder( self, order, dag ):
        self.assertEqual( len( set( order ) ), len( order ) )
        # for any (u, v) in dag, u is before v
        for ( u, v ) in iteredges( dag ):
            self.assertLess( order.index( u ), order.index( v ) )

    def testBfs( self ):
        order = []
        def visit( _, v ):
            order.append( v )

        bfs( self.dag, 0, visit )
        self.assertEqual( set( order ), set( self.dag ) )
        level = i = 0
        while i != ( self.nodes - 1 ):
            j = i + len( self.dag_levels[ level ] )
            self.assertEqual(
                self.dag_levels[ level ], set( order[ i: j ] ) )
            i = j
            level += 1

        order = []
        bfs( self.adj, 0, visit )
        self.assertEqual( set( order ), set( self.adj ) )

    def testDfs( self ):
        def verifyDfsResult( adj, visitRecord ):
            nodes = adj.keys()
            self.assertEqual( len( visitRecord ), len( nodes ) )
            # Test for this is just a sanity check.
            for i, u in enumerate( nodes ):
                visitRecord[ u ].assertValid()
                for j in xrange( i + 1, len( adj ) ):
                    v = nodes[ j ]
                    self.assertFalse(
                        visitRecord[ u ].overlap( visitRecord[ v ] ) )

        visitRecord = dfs( self.adj )
        verifyDfsResult( self.adj, visitRecord )

        visitRecord = dfs( self.dag )
        verifyDfsResult( self.dag, visitRecord )
        reverseRecords = sorted(
            visitRecord.itervalues(), key=lambda r: r.f, reverse=True )
        self.verifyTopologicalOrder(
            [ r.v for r in reverseRecords ], self.dag )

    def testTopoSort( self ):
        self.verifyTopologicalOrder(
            sort_by_dfs_reverse_finish( self.dag ), self.dag )

    def testFindStronglyConnectedComponents( self ):
        self.assertEqual( find_scc( self.adj ), self.components )

    def testCycleDetection( self ):
        self.assertTrue( has_cycle( self.adj ) )
        self.assertFalse( has_cycle( self.dag ) )

    def testBellmanFord( self ):
        pred, records = bellman_ford( self.adj, self.adjw, 0 )
        self.assertEqual( records[ 4 ].w, -3 ) # 0->4's weight
        path = construct_path( pred, 4 )
        self.assertEqual( path, [ 0, 1, 2, 7, 6, 8, 4 ] )

    def testDijkstra( self ):
        pred, records = dijkstra( self.adj, self.adjwp, 0 )
        self.assertEqual( records[ 4 ].w, 7 )
        path = construct_path( pred, 4 )
        self.assertEqual( path, [ 0, 1, 2, 3, 5, 4 ] )

    def testDagShortestPath( self ):
        """BFS is sufficient for exploring all paths in O( V + E ).

        Note: with a cycle, BFS is no longer guaranteed to
        visit all paths and is thus insufficient.
        """
        pred, records = dag_shortest_path( self.dag, self.dagw, 0 )
        self.assertEqual( records[ 8 ].w, 2 )
        path = construct_path( pred, 8 )
        self.assertEqual( path, [ 0, 1, 6, 8 ] )

    @unittest.skip( "write this later with a simple graph of 4 nodes" )
    def testFloydWarshall( self ):
        pass

    def testPrim( self ):
        edges = mst_prim( self.adj_ud, self.adjw_ud )
        self.assertEqual( len( edges ), len( self.adj_ud ) - 1 )
        mst_w = sum( [ self.adjw_ud[ u ][ v ] for ( u, v ) in edges ] )
        self.assertEqual( mst_w, -6 )

    def testKruskal( self ):
        edges = mst_kruskal( self.adj_ud, self.adjw_ud )
        self.assertEqual( len( edges ), len( self.adj_ud ) - 1 )
        mst_w = sum( [ self.adjw_ud[ u ][ v ] for ( u, v ) in edges ] )
        self.assertEqual( mst_w, -6 )

if __name__ == "__main__":
    unittest.main()
