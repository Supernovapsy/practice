import heapq
import numpy as np

class VisitRecord( object ):
    def __init__( self, v, w=np.inf, s=None, f=None ):
        self.v = v
        # weight used for relaxation (if used)
        self.w = w
        # Start and finishing times (if used)
        self.s = s
        self.f = f

    def __repr__( self ):
        return "VisitRecord( {}, w={}, s={}, f={} )".format(
            self.v, self.w, self.s, self.f )

    def __cmp__( self, other ):
        return cmp( self.w, other.w )

    def assertValid( self ):
        assert self.s is not None and self.f is not None

    def overlap( self, other ):
        if self.s < other.s:
            return self.f > other.s and self.f < other.f
        elif self.s > other.s:
            return self.s < other.f and self.f > other.f
        else:
            assert False, "Not expecting any times to be the same."

def construct_path( pred, u ):
    """Return list of nodes from source to u."""
    path = []
    while u is not None:
        path.append( u )
        u = pred[ u ]

    return list( reversed( path ) )

def iteredges( adj ):
    for u in adj:
        for v in adj[ u ]:
            yield u, v

def bfs( adj, s, visit=lambda u, v: None ):
    """Visits adj in BF order using visit().
    Returns the predecessor subgraph.

    visit( u, v ):
        u is the predecessor node, and v is the visited node.

    Note: level-order is basically the same thing as BFS.
    """
    frontier = [ s ]
    next_frontier = []
    visit( None, s )
    pred = { s: None }
    while frontier:
        for u in frontier:
            for v in adj[ u ]:
                if v not in pred:
                    visit( u, v )
                    pred[ v ] = u
                    next_frontier.append( v )
        frontier = next_frontier
        next_frontier = []
    return pred

_dfs_visit_timer = 0

def _dfs_visit( adj, prev, u, visitRecord, visit=lambda u, v: None,
                break_on_cycle_detection=False ):
    global _dfs_visit_timer

    visitRecord[ u ] = VisitRecord( u )
    visitRecord[ u ].s = _dfs_visit_timer
    _dfs_visit_timer += 1
    visit( prev, u )
    for v in adj[ u ]:
        ret = None
        if v not in visitRecord:
            ret = _dfs_visit( adj, u, v, visitRecord, visit,
                              break_on_cycle_detection )
        if ret or ( break_on_cycle_detection and
                    v in visitRecord and visitRecord[ v ].f is None ):
            return True
    visitRecord[ u ].f = _dfs_visit_timer
    _dfs_visit_timer += 1

def dfs( adj, visit=lambda u, v: None ):
    """Returns VisitRecords of all visited nodes, recording down
    starting and visiting times."""
    global _dfs_visit_timer

    visitRecord = {}
    _dfs_visit_timer = 0
    for u in adj:
        if u not in visitRecord:
            _dfs_visit( adj, None, u, visitRecord, visit )

    return visitRecord

def dfs_cycle_detect( adj ):
    """Returns VisitRecords of all visited nodes, recording down
    starting and visiting times."""
    visitRecord = {}
    for u in adj:
        if u not in visitRecord:
            if _dfs_visit( adj, None, u, visitRecord,
                           visit=lambda u, v: None,
                           break_on_cycle_detection=True ):
                return True

    return False

def sort_by_dfs_reverse_finish( adj ):
    visitRecord = dfs( adj )
    reverseRecords = sorted(
        visitRecord.itervalues(), key=lambda r: r.f, reverse=True )
    return [ r.v for r in reverseRecords ]

def find_scc( adj ):
    adjT = { u: [] for u in adj }
    for u in adj:
        for v in adj[ u ]:
            adjT[ v ].append( u )

    scc = set()
    visited = set()
    compRecord = {}
    _dfs_visit_timer = 0
    for u in sort_by_dfs_reverse_finish( adj ):
        if u not in compRecord:
            _dfs_visit( adjT, None, u, compRecord )
            new_scc = set( compRecord ) - visited
            scc.add( frozenset( new_scc ) )
            visited |= new_scc

    return scc

def has_cycle( adj ):
    return dfs_cycle_detect( adj )

def relax( u, v, w, pred=None, mst=False ):
    """Input: VisitRecord for u or v.

    if `pred` is given, it is populated as the predecessor subgraph.
    """
    candidate_w = u.w + w[ u.v ][ v.v ] if not mst else w[ u.v ][ v.v ]
    if candidate_w < v.w:
        if pred:
            pred[ v.v ] = u.v
        v.w = candidate_w

def bellman_ford( adj, w, s ):
    """Returns a predecessor subgraph as well as a dict of
    VisitRecords for each node."""
    pred = { s: None }
    visitRecord = { i: VisitRecord( i ) for i in adj }
    visitRecord[ s ].w = 0

    for _ in range( len( adj ) - 1 ):
        for ( u, v ) in iteredges( adj ):
            relax( visitRecord[ u ], visitRecord[ v ], w, pred )

    # TODO: Add detection for negative-weight cycle.

    return pred, visitRecord

def dijkstra( adj, w, s ):
    """Returns a predecessor subgraph as well as a dict of
    VisitRecords for each node."""
    pred = { s: None }
    visitRecord = { i: VisitRecord( i ) for i in adj }
    visitRecord[ s ].w = 0

    q = visitRecord.values()
    while q:
        r = heapq.heappop( q )
        for v in adj[ r.v ]:
            relax( r, visitRecord[ v ], w, pred )
        # TODO: This can be optimized by using min_heapify
        heapq.heapify( q )

    return pred, visitRecord

def dag_shortest_path( adj, w, s ):
    visitRecord = { i: VisitRecord( i ) for i in adj }
    visitRecord[ s ].w = 0

    def visit( u, v ):
        if u is not None:
            relax( visitRecord[ u ], visitRecord[ v ], w )

    return bfs( adj, s, visit ), visitRecord

def mst_prim( adj, w ):
    if not adj:
        return # no elements

    visitRecord = { i: VisitRecord( i ) for i in adj }

    q = visitRecord.values()
    q[ 0 ].w = 0
    pred = { q[ 0 ].v: None }

    mst = set()
    while q:
        r = heapq.heappop( q )
        u = r.v
        if pred[ u ] is not None: # If not the source node
            mst.add( ( pred[ u ], u ) )
        for v in adj[ u ]:
            relax( visitRecord[ u ], visitRecord[ v ], w, pred, mst=True )
        heapq.heapify( q )

    return mst

def mst_kruskal( adj, w ):
    mst = set()

    # { node: set_id }
    set_id = { u: u for u in adj }
    # { set_id: { set elements } }
    set_map = { u: { u } for u in adj }

    def edge_cmp( e1, e2 ):
        u, v = e1
        x, y = e2
        return cmp( w[ u ][ v ], w[ x ][ y ] )

    for edge in sorted( iteredges( adj ), cmp=edge_cmp ):
        u, v = edge
        if w[ u ][ v ] == np.inf:
            break # We have looked at all edges.
        u_id, v_id = set_id[ u ], set_id[ v ]
        if u_id != v_id:
            if len( set_map[ u_id ] ) > len( set_map[ v_id ] ):
                smaller_id, bigger_id = v_id, u_id
            else:
                smaller_id, bigger_id = u_id, v_id

            for k in set_map[ smaller_id ]:
                set_map[ bigger_id ].add( k )
                set_id[ k ] = bigger_id
            del set_map[ smaller_id ]
            mst.add( edge )

    return mst
