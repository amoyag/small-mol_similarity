"""
Function: geometric(graph,xnodes,ynodes)

Compute Geometric association index Fuxman Bass et al., 2013. Nature methods, 10(12):1169

aurelio.moya@ucl.ac.uk
---------------------------------

"""

import math
from networkx.algorithms import bipartite
from networkx import *
from decimal import *
import numpy

def geometric(G,u,v):
    unbrs = set(G[u])
    vnbrs = set(G[v])
    return float((len(unbrs & vnbrs))^2) / (len(unbrs) * len(vnbrs))