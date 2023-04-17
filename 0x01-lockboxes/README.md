## 0x01. Lockboxes

This program contains a function canUnlockAll(boxes) that determines whether or not all the locked boxes in a list of boxes can be opened by their respective keys.
# Usage

The canUnlockAll(boxes) function takes one argument boxes, which is a list of lists containing a key to locked boxes. Each box is represented by a list, and the keys to the other boxes are represented as integers in the list. The first box (index 0) is unlocked and does not require a key.

The function returns True if all the boxes can be opened, and False otherwise.
Example

```python

 boxes = [[1], [2], [3], [4], []]
 canUnlockAll(boxes)
True
```

In this example, there are 5 boxes, and each box contains a key to the next box. The last box is unlocked and does not require a key. The canUnlockAll(boxes) function returns True because all the boxes can be opened.

## Requirements

This program requires no external libraries or modules to be installed.
