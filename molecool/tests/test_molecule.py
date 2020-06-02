'''
Unit and regression test for the molecule module
'''

import molecool
import numpy as np
import pytest


@pytest.fixture
def methane_molecule():

    symbols = ['C', 'H', 'H', 'H', 'H']
    coordinates = np.array([
    [1, 1, 1],
    [2.4, 1, 1],
    [-0.4, 1, 1],
    [1, 1, 2.4],
    [1, 1, -0.4]
    ])

    return symbols, coordinates

#def test_move_methane(methane_molecule):
#    #demostration of @pytest.fixture(scope='module')
#    symbols, coordinates = methane_molecule
#
#    coordinates[0] += 5

def test_build_bond_list(methane_molecule):

    symbols, coordinates = methane_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4

def test_molecular_mass(methane_molecule):

    symbols, coordinates = methane_molecule
    #symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass


def test_center_of_mass(methane_molecule):

    symbols, coordinates = methane_molecule

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert np.array_equal(center_of_mass, expected_center)
