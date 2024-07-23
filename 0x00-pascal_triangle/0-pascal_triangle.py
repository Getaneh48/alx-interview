#!/usr/bin/python3
"""
a function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    triangle = []
    if n <= 0:
        return triangle

    for r in range(0, n):
        if r == 0:
            triangle.append([1])
        elif r == 1:
            triangle.append([1, 1])
        else:
            ind = r - 1
            prev_row = triangle[ind]
            new_row = [1]
            for j, v in enumerate(prev_row):
                if j + 1 < len(prev_row):
                    new_row.append(prev_row[j] + prev_row[j + 1])
            new_row.append(1)
            triangle.append(new_row)
    return triangle
