#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Lockboxes """
    for j in range(1, len(boxes)):
        state = False
        for i in range(len(boxes)):
            if j in boxes[i] and j != i:
                state = True
                break
        if not state:
            return state

    return True
