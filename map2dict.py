
"""
Function: map2dict(mapfile)

Creates small molecule - target dictionary from mapping file
Compute PCC assoc index of small molecules

aurelio.moya@ucl.ac.uk
---------------------------------

"""   

def map2dict(mapfile):
    import numpy
    comp_target = {}
    dPfile = open(mapfile, 'r')
    lines = dPfile.readlines()
    numpy.array(lines)
    dPfile.close() 
    for line in lines:
        line = line.replace("\n", "")
        vals = line.split("\t")
        drug = vals[2]
        target = vals[1]
        if not comp_target.has_key(drug): comp_target[drug] = []
        if not target in comp_target[drug]: comp_target[drug].append(target)
    return(comp_target)    
       