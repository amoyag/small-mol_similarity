"""
Function: cosine(graph,xnodes,ynodes)

Compute Cosine association index Fuxman Bass et al., 2013. Nature methods, 10(12):1169

aurelio.moya@ucl.ac.uk
---------------------------------

"""
import math
from networkx.algorithms import bipartite
from networkx import *
from decimal import *
import numpy

def cosine(G,u,v):
    unbrs = set(G[u])
    vnbrs = set(G[v])
    return float(len(unbrs & vnbrs)) / (math.sqrt(len(unbrs) * len(vnbrs)))