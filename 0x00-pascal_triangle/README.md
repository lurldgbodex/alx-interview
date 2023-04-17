# 0x00. Pascal's Triangle

This program contains a function pascal_triangle(n) that returns a list of lists of integers representing the Pascal's triangle of n.

## Usage

The pascal_triangle(n) function takes one argument n which is an integer. It returns a list of n lists, each containing i+1 integers, where i is the index of the list in the outer list. The first and last integers of each list are always 1, and each subsequent integer is the sum of the two integers directly above it in the previous list.

If n is less than or equal to 0, the function returns an empty list.

## Example

```python 
pascal_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Requirements

This program requires no external libraries or modules to be installed.
