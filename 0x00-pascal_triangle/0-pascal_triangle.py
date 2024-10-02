#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Build each subsequent row based on the previous one
    for i in range(1, n):
        prev_row = triangle[-1]
        # Generate a new row using values from the previous row
        row = [1]  # Every row starts with a 1
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Every row ends with a 1
        triangle.append(row)

    return triangle
