#!/usr/bin/python3
'''
    0x01. Lockboxes
'''

def canUnlockAll(boxes)
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or