'''
Functions for visualization of molecules.
'''


import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from .atom_data import atom_colors


def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    '''
    Draw a picture of a molecule using Matplotlib.

    Parameters
    ----------
    coordinates : np.ndarray
        Coordinates of each atom as a 2D numpy array.
    symbols : list
        Element symbols for each atom.
    draw_bonds : dict
        Bond_list of bonds to draw. Tuple of the two atoms index in coordinates as keys, bond length as value. Default None.
    save_location : str
        Location where the image of the drawn molecule is saved. Default None.
    dpi : int
        Resolution of the saved image file. Only applies if save_location is provided. Default 300.

    Returns
    -------
    ax : matplotlib.axes.Axes3D
        3D-Axes object containing the molecule image.
    '''

    if len(coordinates) != len(symbols):
        raise ValueError(f'molecool.draw_molecule - unequal number of coordinates ({len(coordinates)}) and symbols ({len(symbols)})')

    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])

    size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))

    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
               edgecolors='k', facecolors=colors, alpha=1, s=size)

    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]

            ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
                    coordinates[[atom1,atom2], 2], color='k')

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)

    return ax

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    '''
    Draw a histogram of bond lengths based on a bond_list (output from build_bond_list function)

    Parameters
    ----------
    bond_list : dict
        Keys are tuples of atom bond indices. Values are bond lengths.
    save_location : str
        Location where the image of the drawn molecule is saved. Default None.
    dpi : int
        Resolution of the saved image file. Only applies if save_location is provided. Default 300.
    graph_min : float
        Minumum of the histogram bin range. Default 0.
    graph_max : float
        Maximum of the histogram bin range. Default 2.

    Returns
    -------
    ax : matplotlib.axes.Axes
        Axes object containing the bond histogram.
    '''

    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)

    bins = np.linspace(graph_min, graph_max)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')


    ax.hist(lengths, bins=bins)

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)

    return ax
