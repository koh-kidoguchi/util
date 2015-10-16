import csv
import make_link

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2, node3) in tsv:
        actors = node1.split(', ')
        if len(actors) == 2:
            make_link.make_link(G, actors[0], actors[1])
    return G
