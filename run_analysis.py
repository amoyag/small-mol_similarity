


import numpy
import map2dict
import bipartg
import fingerprints




if __name__ == '__main__':
    import sys

    if len(sys.argv) < 1:  # the program name and one argument

        sys.exit("Must specify path to mapping file")


    mapfile = sys.argv[1]
    


# comp_target = map2dict.map2dict('../mapChEMBLPfam/data/map_pfam.txt')
comp_target = map2dict.map2dict(mapfile)
edges = bipartg.bipartg(comp_target)

fingerprints.fingerp(edges)

