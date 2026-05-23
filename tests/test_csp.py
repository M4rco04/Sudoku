import pytest
import numpy as np
import copy

from csp.csp import CSP
from representation.board import Board

@pytest.fixture
def board():
    return Board("01.txt")

@pytest.fixture
def csp(board: Board):
    return CSP(board)

def test_number_of_assigments(csp: CSP):
    assert csp.assigments == 81 - 32

def test_domain(csp: CSP):
    assert csp.domains[0, 0] == {4, 5}
    assert csp.domains[7, 4] == {4, 5, 7}

def test_count_active_peers(csp: CSP):
    assert csp.count_active_peers((0, 0)) == 13
    assert csp.count_active_peers((3, 5)) == 11

def test_select_unassigned_variable(csp: CSP):
    assert csp.select_unassigned_variable() == (8, 3)

def test_order_domain_values(csp: CSP):
    assert csp.order_domain_values((8, 3)) == [4]