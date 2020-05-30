'''
Unit and regression test for the measure module
'''

import molecool
import numpy as np

def test_calculate_distance():

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 0, 1])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert calculated_distance == expected_distance

def test_calculate_angle():

    rA = np.array([0, 0, 1])
    rB = np.array([0, 0, 0])
    rC = np.array([0, 1, 0])

    expected_angle = 90. # in degrees

    calculated_angle = molecool.calculate_angle(rA, rB, rC, degrees=True)

    assert calculated_angle == expected_angle
