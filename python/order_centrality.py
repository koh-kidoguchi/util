from read_graph import read_graph
from centrality import centrality
from build_heap import build_heap
from down_heap import down_heapify

def order_centrality(G):

    ctrs = {}
    for actor in G.keys():
        ctrs[actor] = centrality(G, actor)

    # print ctrs
    elems = ctrs.values()
    G = build_heap(elems)

    min = 0
    for i in range(1):
        min = G[0]
        G[0] = G[len(G)-1]
        G.pop()
        down_heapify(G, 0)

    return min

#test
G = read_graph('file.tsv')
print order_centrality(G)
