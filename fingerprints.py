

"""
Function fingerp()

Computes fingerprint similarity between two compounds a and b

aurelio.moya@ucl.ac.uk
-----------------------

"""


# def fingerp(a,b):
#     import rdkit
#     from rdkit import Chem
#     from rdkit.Chem import AllChem
#     from rdkit import DataStructs
#     from rdkit.Chem.Fingerprints import FingerprintMols
#     import subprocess
#     # Generates a file with mol sdf for the two compounds with a shell script
#     subprocess.call(["/Users/aurelio/sandbox/drugDomain_map/drugsimil/getsdf2.sh", a, b])
#     # Dictionary MOLREGNO:Fingerprint and Fingerprint similarity
#     fingerprints = {}
#     sdffile = open('./drug.sdf', 'r')
#     rd = Chem.ForwardSDMolSupplier(sdffile, sanitize=True)
#     for mol in rd:
#         if not fingerprints.has_key(mol.GetProp('MOLREGNO')):fingerprints[mol.GetProp('MOLREGNO')] = FingerprintMols.FingerprintMol(mol)
#     fpa = fingerprints[a]
#     fpb = fingerprints[b]
#     simil = DataStructs.FingerprintSimilarity(fpa,fpb)
#     sdffile.close()
#     return(simil)



def fingerp(edges):
    import rdkit
    from rdkit import Chem
    from rdkit.Chem import AllChem
    from rdkit import DataStructs
    from rdkit.Chem.Fingerprints import FingerprintMols
    import shellmysql
    import os
    nodes = []
    # nodesfile = open('nodes.txt', 'wb')
    for tupla in edges:
        for node in tupla:
            if not node in nodes:
                nodes.append(node)
                # nodesfile.write("%s\n" %(node))
    shellmysql.shellmysql(nodes)
    fingerprints = {}
    sdffile = open('./drug.sdf', 'r')
    rd = Chem.ForwardSDMolSupplier(sdffile, sanitize=True)
    for mol in rd:
        if not fingerprints.has_key(mol.GetProp('MOLREGNO')):fingerprints[mol.GetProp('MOLREGNO')] = FingerprintMols.FingerprintMol(mol)
    simil = open ("./results/similarity.txt" ,"wb")    
    for tupla in edges:
        fpa = fingerprints[tupla[0]] 
        fpb = fingerprints[tupla[1]] 
        sim = DataStructs.FingerprintSimilarity(fpa,fpb)
        simil.write("%s\t%s\t%.3f\n" %(tupla[0], tupla[1], sim)) 
    sdffile.close()
    os.remove('./drug.sdf')             