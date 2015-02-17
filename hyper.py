"""
Function: hypergeometric(graph,xnodes,ynodes)

Compute Hypergeometric association index Fuxman Bass et al., 2013. Nature methods, 10(12):1169

aurelio.moya@ucl.ac.uk anibal.bueno@uma.es bserrano@uma.es
---------------------------------

"""

import math
from networkx.algorithms import bipartite
from networkx import *
from decimal import *
import numpy

def productorio(mayor, menor):
    resultado = 1
    for i in xrange(mayor, menor, -1):
	resultado = resultado * i
    return resultado

def hypergeometric(G,u,v):
    bottom_nodes, top_nodes = bipartite.sets(B)
    unbrs = set(G[u])
    vnbrs = set(G[v])
    init = len(unbrs & vnbrs)
    NA = len(unbrs)
    NB = len(vnbrs)
    end = min(NA,NB)
    output = 0
    ny = len(bottom_nodes)
    #print init
    #print end
    for i in xrange(init, end+1, 1):
	half = NA/2
	
	if(i > half):
	    new_NA=productorio(NA,i)
	    new_i=math.factorial(NA-i)
	else:
	    new_NA=productorio(NA,NA-i)
	    new_i=math.factorial(i)
	num1=new_NA/new_i
        
	#num1 = math.factorial(math.factorial(NA)) / (math.factorial(i) * math.factorial(NA - i))

	up=ny-NA
	down=NB-i
	
	half2 = up/2
	
	if(down > half2):
	    new_up=productorio(up,down)
	    new_down=math.factorial(up-down)
	else:
	    new_up=productorio(up,up-down)
	    new_down=math.factorial(down)
	num2=new_up/new_down	

        #num2 = math.factorial(math.factorial(ny - NA)) / (math.factorial(NB - i) * math.factorial(ny - NA - NB + i))

	half3 = ny/2

	if(NB > half3):
	    new_ny=productorio(ny,NB)
	    new_NB=math.factorial(ny-NB)
	else:
	    new_ny=productorio(ny,ny-NB)
	    new_NB=math.factorial(NB)
	den=new_ny/new_NB

        #den = math.factorial(ny) / (math.factorial(NB) * math.factorial(ny - NB))
	#print num1
	#print num2
	numerador=num1*num2
	#print numerador
	#print den
	resu = Decimal(numerador)/Decimal(den)
	#print resu
        output += resu
	#print output
    #print numerador
    #print den
    #print output
    return -math.log10(output)	