import geom_analysis as ga
import pytest

def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    expected = 1.0
    observed = ga.calculate_distance(coord1,coord2)
    assert observed == expected

def test_bond_check():
    atom_distance = 1.5
    expected = True
    observed = ga.bond_check(atom_distance)
    assert observed == expected
 # edge case 0 returns False, edge case 1.5 returns True

def test_bond_check():
     atom_distance = 1.5
     expected = True
     observed = ga.bond_check(atom_distance)
     assert observed == expected

def test_bond_check_edge0():
    atom_distance = 0
    expected = False
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_bond_check_edge1_5():
    atom_distance = 1.5
    expected = True
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_bond_check_edge_2_5():
    atom_distance = 2.5
    expected = False
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_bond_check_negative1():
    atom_distance = -1
    expected = False
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_bond_check_negative2():
    atom_distance = -1
    expected = False
    with pytest.raises(ValueError):
        calculated = ga.bond_check(distance)
    assert observed == calculated
