#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
        boxes: A list of lists, where each inner list
        contains keys to other boxes.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    n = len(boxes)
    visited = set()  # Use a set for efficient membership checks

    def dfs(box):
        if box in visited:
            return
        visited.add(box)
        for key in boxes[box]:
            if 0 <= key < n:
                dfs(key)

    dfs(0)  # Start from the first box
    return len(visited) == n
