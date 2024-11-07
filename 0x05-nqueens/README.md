# Pascal's Triangle

## Description
This project implements a function `pascal_triangle(n)` that returns a list of lists representing Pascal’s Triangle of a given size `n`. Each row in Pascal's Triangle is constructed by adding adjacent elements from the previous row.

## Requirements
- **Python 3**
- Return an empty list if `n <= 0`.
- Output should be a list of lists representing Pascal’s Triangle.

## Example
```python
>>> pascal_triangle(5)
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
