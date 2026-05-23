import numpy as np
import copy

from typing import Tuple, List, Set
import numpy.typing as npt

from representation.board import Board

class CSP:
    board: Board
    assigments: int
    variables: npt.NDArray[np.int8]
    domains: npt.NDArray[np.object_]

    def __init__(self, board: Board):
        self.board = board
        self.assigments = 81 - np.count_nonzero(board.board)
        self.variables = copy.deepcopy(self.board.board)
        self._set_domain()
    

    def get_neighbours(self, var: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbours = self.board.block_index(var) | self.board.col_index(var) | self.board.row_index(var)
        neighbours -= {var}
        return neighbours


    def constrain(self, var: Tuple[int, int]) -> Set[int]:
        allow_values = set(range(1, 10))
        used_values = set([self.variables[var_j] for var_j in self.get_neighbours(var)])
        return allow_values - used_values
    

    def assign(self, var: Tuple[int, int], val: np.int8) -> bool:
        if val not in self.constrain(var):
            return False
        self.variables[var] = val
        return self._update_domains(var, val)


    def consistant(self, var: Tuple[int, int], val: np.int8) -> bool:
        if val not in self.constrain(var):
            return False
        return True
    
    
    def _update_domains(self, var: Tuple[int, int], val: np.int8) -> bool:
        self.domains[var] = {val}
        for var_j in self.get_neighbours(var):
            self.domains[var_j] -= {val}
            if len(self.domains[var_j]) == 0:
                return False
        return True


    def _set_domain(self) -> bool:
        self.domains = np.empty(shape=(9, 9), dtype=np.object_)
        board = self.board.board

        for var in self.board.flat_board():
            if board[var] != 0:
                self.domains[var] = {board[var]}
                continue

            self.domains[var] = self.constrain((var))
            if len(self.domains[var]) == 0:
                return False
        return True
    

    def count_active_peers(self, var: Tuple[int, int]) -> int:
        active = 0
        for var_j in self.get_neighbours(var):
            if self.variables[var_j] == 0:
                active += 1
        
        return active


    def select_unassigned_variable(self) -> Tuple[int, int]:
        min_domain_size = float("inf")
        max_degree = -1

        for var in self.board.flat_board():
            if self.variables[var] != 0:
                continue
            if len(self.domains[var]) < min_domain_size:
                unassigned = var
                min_domain_size = len(self.domains[var])
                max_degree = self.count_active_peers(var)
            elif len(self.domains[var]) == min_domain_size:
                if max_degree <= self.count_active_peers(var):
                    continue
                unassigned = var
                max_degree = self.count_active_peers(var)                
        
        return unassigned
    
    
    def order_domain_values(self, var: Tuple[int, int]) -> List[int]:
        values = list(self.domains[var])

        if len(values) <= 1:
            return values

        def count_conflicts(val):
            count = 0
            for var_j in self.get_neighbours(var):
                if self.variables[var_j] == 0 and val in self.domains[var_j]:
                    count += 1
            
            return count

        return sorted(values, key=count_conflicts)