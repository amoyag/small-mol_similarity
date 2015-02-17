"""
Function: bipartg(dictionary)

Build a bipartite graph from a small molecule - target dictionary.
Compute PCC assoc index of small molecules using function pcc

Function: pcc(graph,xnodes,ynodes)

Compute association index based on Pearson Correlation Coefficient of interaction pro files Fuxman Bass et al., 2013. Nature methods, 10(12):1169

aurelio.moya@ucl.ac.uk
---------------------------------

"""
from decimal import *
from networkx import *
def bipartg(dictionary):
    import math
    from networkx.algorithms import bipartite
    
    def pcc(G,u,v):
       ny = len(bottom_nodes)
       unbrs = set(G[u])
       vnbrs = set(G[v])
       return (float(len(unbrs & vnbrs)) * ny - (len(unbrs) * len(vnbrs))) / (math.sqrt((len(unbrs) * len(vnbrs)) * (ny - len(unbrs)) * (ny - len(vnbrs)))) 
 
    B = Graph()
    for drug in dictionary.keys():
        for element in dictionary[drug]:
            B.add_node(drug, bipartite=0)
            B.add_node(element, bipartite=1)
            B.add_edge(element, drug)
    top_nodes = set(n for n,d in B.nodes(data=True) if d['bipartite']==0)
    bottom_nodes = set(n for n,d in B.nodes(data=True) if d['bipartite']==1)
    #bottom_nodes = set(B) - top_nodes # Alternative way to define bottom nodes

    drugs=list(top_nodes)
    targets=list(bottom_nodes)
    print ("check that ", drugs[30], " is a drug")   
    J = bipartite.generic_weighted_projected_graph(B, top_nodes, weight_function=pcc)
    edges = J.edges()
    # print edges[30]
    write_weighted_edgelist(J, "./results/pcc.txt", delimiter="\t")
    return(edges) 
