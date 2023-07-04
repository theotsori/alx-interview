#!/usr/bin/python3
"""
Function that checks if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list
        represents a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    keys = [0]

    while keys:
        new_key = keys.pop()
        for box in boxes[new_key]:
            if 0 <= box < num_boxes and not unlocked[box]:
                unlocked[box] = True
                keys.append(box)

    return all(unlocked)
