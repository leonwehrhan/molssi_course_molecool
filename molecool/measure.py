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
    #if dist == 0.:
        #raise Exception('Two atoms are located in the same point.')
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    '''
    Calculate the angle between three points.

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        Coordinate of each point of the angle ABC.
    degrees : bool
        If False (default), result is given in radians. If True, result is given in degrees.

    Returns
    -------
    theta : float
        Angle ABC in radians (default) or degrees if specified.
    '''
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
