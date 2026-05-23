import argparse

from algorithm.backtracking_search import Backtracking_search
from csp.csp import CSP
from representation.board import Board

def main():
    parser = argparse.ArgumentParser(description="Rozwiązywanie problemu N-Puzzels")
    parser.add_argument("-f", "--file", help="Plik, z którego wczytywane są puzzle")
    args = parser.parse_args()


    if not args.file:
        raise ValueError("Nie podano pliku")

    board = Board(args.file)
    csp = CSP(board)
    bs = Backtracking_search(csp)

    bs.solve()
    bs.draw_sudoku()

if __name__ == "__main__":
    main()