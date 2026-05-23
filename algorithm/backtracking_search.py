from typing import Dict, Tuple

from datetime import datetime
import copy

from representation.board import Board
from csp.csp import CSP

class Backtracking_search:
    csp: CSP
    assigment: Dict[Tuple[int, int], int]

    def __init__(self, csp: CSP):
        self.csp = csp
        self.assigment = None


    def solve(self):
        start = datetime.now()
        assigment = self._search(self.csp, {})
        self.time = (datetime.now() - start).total_seconds()
        self.assigment = assigment
        return assigment
    
    def _search(self, csp: CSP, assigment: Dict[Tuple[int, int], int]) -> Dict[Tuple[int, int], int] | None:
        if len(assigment) == csp.assigments:
            return assigment
        
        unassigned = csp.select_unassigned_variable()
        for value in csp.order_domain_values(unassigned):
            local_assigment = assigment.copy()
            local_assigment[unassigned] = value

            if csp.consistant(unassigned, value):
                local_csp = copy.deepcopy(csp)
                local_csp.assign(unassigned, value)
                result = self._search(local_csp, local_assigment)
                if result is not None:
                    return result
        
        return None            
    
    def draw_sudoku(self):
        if self.assigment == None:
            print("It's no solution for this sudoku")
            return
        print("|-------"*3 + "|")
        for id, var in enumerate(self.csp.board.flat_board()):
            if id % 3 == 0:
                print("|", end=" ")
            if self.csp.variables[var] != 0:
                print(self.csp.variables[var], end=" ")
            else:
                print(self.assigment[var], end=" ")
            if (1 + id) % 9 == 0:
                print("|")
            if (1 + id) % 27 == 0:
                print("|-------"*3 + "|")
                
            
