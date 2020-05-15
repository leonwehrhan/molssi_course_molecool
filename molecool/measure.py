'''
This module is for functions which perform measurements.
'''


import numpy as np


def calculate_distance(rA, rB):
    '''
    Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 0.0, 1.0])
    >>> calculate_distance(r1, r2)
    1.0
    '''

    if isinstance(rA, np.ndarray) is False or isinstance(rB, np.ndarray) is False:
        raise TypeError('rA and rB must be numpy arrays.')

    d=(rA-rB)
    dist=np.linalg.norm(d)
    if dist == 0:
        raise Exception('Two atoms are located in the same point.')
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
