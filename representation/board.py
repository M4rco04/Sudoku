import numpy as np

import numpy.typing as npt
from typing import Set, Tuple

class Board:
    file: str
    board: npt.NDArray[np.int8]

    def __init__(self, filename: str):
        self.file = filename
        self.board = np.zeros(shape=(9, 9), dtype=np.int8)
        self._read_file()

    def _read_file(self) -> None:
        with open(f"data/{self.file}", "r") as file:
            for x, row in enumerate(file):
                row = row.strip()
                for y, cell in enumerate(row.split(" ")):
                    cell = int(cell)
                    if cell == 0:
                        continue
                    self.board[x][y] = cell
    
    def get_block(self, var: Tuple[int, int]) -> npt.NDArray[np.int8]:
        x_start, y_start = 3 * (var[0] // 3), 3 * (var[1] // 3)
        return self.board[x_start:x_start+3, y_start:y_start+3]


    def block_index(self, var: Tuple[int, int]) -> Set[Tuple[int, int]]:
        x_start, y_start = 3 * (var[0] // 3), 3 * (var[1] // 3)
        return set([
            (x, y)
            for x in range(x_start, x_start + 3)
            for y in range(y_start, y_start + 3)
        ])
    
    def row_index(self, var: Tuple[int, int]) -> Set[Tuple[int, int]]:
        return set(
            [(var[0], y) for y in range(0, 9)]
        )
    

    def get_row(self, var: Tuple[int, int]) -> npt.NDArray[np.int8]:
        return self.board[var[0], :]
    

    def col_index(self, var: Tuple[int, int]) -> Set[Tuple[int, int]]:
        return set(
            [(x, var[1]) for x in range(0, 9)]
        )
    
    def get_col(self, var: Tuple[int, int]) -> npt.NDArray[np.int8]:
        return self.board[:, var[1]]
    
    def flat_board(self) -> Tuple[Tuple[int, int]]:
        return tuple([
            (x, y) 
            for x in range(0, 9)
            for y in range(0, 9) 
        ])