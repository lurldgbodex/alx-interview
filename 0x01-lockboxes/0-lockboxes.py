#!/usr/bin/python3
'''determines if boxes can be opened'''


def canUnlockAll(boxes):
    '''determines if all locked boxes can be opened
    args:
        boxes: list of lists containing a key
          to locked boxes.
    return:
        True if all boxes can be opend and false
            otherwise.'''
    length = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        box_idx = locked_boxes.pop()
        if not box_idx or box_idx >= length or box_idx < 0:
            continue
        if box_idx not in unlocked_boxes:
            locked_boxes = locked_boxes.union(boxes[box_idx])
            unlocked_boxes.add(box_idx)
    return length == len(unlocked_boxes)
