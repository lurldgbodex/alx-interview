# 0x02. Minimum Operations

This program contains a function minOperations(n) that calculates the fewest number of operations needed to result in exactly n H characters in the file.

## Usage

The minOperations(n) function takes one argument n, which is an integer representing the number of H's you want to achieve. The function returns an integer representing the fewest number of operations needed to achieve n H's.

An operation is defined as either of the following:

    Copy all the H's.
    Paste the copied H's one by one.

## Example

```python

>>> minOperations(9)
6
```

In this example, we want to achieve 9 H's using the copy and paste operations. The minOperations(n) function returns 6 because it takes 2 operations to copy the initial H's (2 operations), and 4 operations to paste them to get 9 H's.

## Requirements

This program requires no external libraries or modules to be installed.
