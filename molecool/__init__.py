"""
molecool
A Python package for analyzing and visualizing pdb and xyz files. For MolSSI May webinar series.
"""

# Add imports here
from .functions import *
from .molecule import build_bond_list
from .measure import calculate_distance, calculate_angle
from .visualize import draw_molecule, bond_histogram
from .atom_data import atomic_weights, atom_colors

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
