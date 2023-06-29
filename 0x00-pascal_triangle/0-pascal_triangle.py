#!/usr/bin/python3
"""
function that generates pascal's triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle.

    Raises:
        None.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        p_row = triangle[i - 1]
        c_row = [1]

        for j in range(1, i):
            c_row.append(p_row[j - 1] + p_row[j])

        c_row.append(1)
        triangle.append(c_row)

    return triangle
