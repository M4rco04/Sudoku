import pytest
import numpy as np

from representation.board import Board

@pytest.fixture
def board():
    return Board("01.txt")

@pytest.fixture
def sudoku():
    return np.array([
        [0, 0, 3, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0],
    ], dtype=np.int8) 

@pytest.fixture
def block():
    return np.array([
        [6, 0, 9],
        [2, 0, 3],
        [0, 1, 0]
    ], dtype=np.int8)

@pytest.fixture
def row():
    return np.array(
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
    dtype=np.int8)

@pytest.fixture
def col():
    return np.array(
        [3, 0, 1, 8, 0, 6, 2, 0, 5],
    dtype=np.int8)

def test_init(board: Board, sudoku):
    assert np.array_equal(board.board, sudoku)

def test_get_block(board: Board, block):
    assert np.array_equal(board.get_block((7, 4)), block)

def test_get_row(board: Board, row):
    assert np.array_equal(board.get_row((5, 3)), row)

def test_get_column(board: Board, col):
    assert np.array_equal(board.get_col((8, 2)), col)

def test_block_index(board: Board):
    assert np.array_equal(board.block_index((4, 5)),
        {(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)})