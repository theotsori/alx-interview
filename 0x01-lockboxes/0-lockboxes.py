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

    for box_index in keys:
        unlocked[box_index] = True

        for new_key in boxes[box_index]:
            if new_key not in keys:
                keys.append(new_key)

    for status in unlocked:
        if not status:
            return False

    return True
