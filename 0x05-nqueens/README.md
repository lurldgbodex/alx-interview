# 0x05. N Queens

This is a Python script to solve the N-Queen problem using a recursive algorithm. The N-Queen problem consists of placing N chess queens on an N×N chessboard so that no two queens threaten each other.

## Usage

To use the script, run the following command in your terminal:

```bash

 ./0-nqueens.py N
```
where N is an integer greater or equal to 4, representing the number of queens and the size of the board.
Output

The script will output all the possible solutions to the problem in the format of a list of pairs representing the position of each queen on the board. For example, the output for N=4 would be:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
where each pair [i, j] represents a queen placed in row i and column j.

## How it works

The script uses a recursive backtracking algorithm to place the queens on the board. The algorithm starts by placing the first queen in the first column of the first row. Then, it tries to place the second queen in the second row, and so on until it places the last queen in the last row.

At each step, the algorithm checks if the queen can be placed in a certain row and column without threatening the queens that were already placed on the board. If it can, it places the queen and moves on to the next row. If it cannot, it backtracks to the previous row and tries to place the queen in another column.

The algorithm stops when it places all the queens on the board, and it records the positions of the queens in a list. It then backtracks to the previous row and tries to place the queen in another column.

The algorithm continues until it exhausts all the possible solutions.
