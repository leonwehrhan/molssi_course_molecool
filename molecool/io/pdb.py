'''
Functions for manipulating pdb files.
'''

import numpy as np



def open_pdb(f_loc):
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            try:
                c2 = [float(x) for x in l[30:55].split()]
            except ValueError as e:
                raise ValueError(f'Error in pdb file {f_loc}. Could not read coordinates.\n {e}')
            c.append(c2)
    coords = np.array(c)
    return sym, coords