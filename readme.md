# Sudoku Solver - Constraint Satisfaction Problem (CSP)

This project is an implementation of a Sudoku solving tool in Python. It utilizes modeling based on the **CSP - Constraint Satisfaction Problem** and the **Backtracking Search** algorithm.

To optimize the solving process, the following heuristics have been implemented in the project:

* **MRV (Minimum Remaining Values):** First selects the empty cell (variable) that has the fewest allowed values remaining.
* **Degree Heuristic:** Used as a tie-breaker for MRV. It selects the variable that is involved in the largest number of constraints with other unassigned variables.
* **LCV (Least Constraining Value):** Orders the value domains to first check the numbers that least restrict the available choices for neighboring empty cells.

---

## 🛠 Requirements

To run the project, **Python 3.x** and the **NumPy** library are required.

You can install missing dependencies using the `pip` package manager:

```bash
pip install numpy

```

---

## 📂 Project Structure

The project has been divided into modules to ensure code readability and maintainability:

* `main.py` - The main entry point of the application. Responsible for parsing command-line arguments and starting the solving process.
* `algorithm/backtracking_search.py` - Implementation of the Backtracking algorithm. Responsible for the process of finding the solution and rendering the result in the console.
* `csp/csp.py` - Definition of the CSP problem. Manages domains, constraints between cells, verifies consistency, and contains the logic for the MRV and LCV heuristics.
* `representation/board.py` - Representation of the Sudoku board. Responsible for loading data from a text file and providing helper methods for indexing rows, columns, and 3x3 blocks.

---

## 🚀 How to Run

To run the solver, use the `main.py` file, passing the `-f` (or `--file`) flag along with the name of the text file containing the board as an argument.

**Important:** According to the project assumptions, board files must be located in the `data/` directory within the main project folder.

### Example Usage

```bash
python main.py -f 04.txt

```

---

## 📝 Input File Format

The text file (e.g., `04.txt`) representing the board should consist of 9 lines.

Each line contains 9 numbers separated by a single space.

* Numbers from `1` to `9` represent pre-assigned values.
* `0` (zero) represents an empty cell to be solved.

### Example File Layout

```text
2 0 4 0 0 0 0 0 5
0 7 8 0 0 1 0 0 0
9 0 0 0 0 0 3 0 0
0 0 0 0 2 6 0 0 4
0 0 0 0 7 0 0 0 9
0 0 0 0 5 0 7 8 0
0 9 0 0 0 0 0 6 2
4 0 0 6 0 0 0 0 8
0 1 0 0 0 8 0 0 0

```

---

## 📊 Output

After successfully solving the puzzle, the program will draw the complete Sudoku board in the console, divided into a 3x3 grid, for example:

```text
|-------|-------|-------|
| 2 3 4 | 9 6 7 | 8 1 5 |
| 5 7 8 | 3 4 1 | 2 9 6 |
| 9 6 1 | 2 8 5 | 3 4 7 |
|-------|-------|-------|
| 7 8 9 | 1 2 6 | 5 3 4 |
| 1 4 5 | 8 7 3 | 6 2 9 |
| 3 2 6 | 4 5 9 | 7 8 1 |
|-------|-------|-------|
| 8 9 7 | 5 3 4 | 1 6 2 |
| 4 5 3 | 6 1 2 | 9 7 8 |
| 6 1 2 | 7 9 8 | 4 5 3 |
|-------|-------|-------|

```

If the given Sudoku data has no solution, the program will display an appropriate message.
