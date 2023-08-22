# Rotating a 2D Matrix by 90 Degrees Clockwise

Rotating a 2D matrix by 90 degrees clockwise involves rearranging the elements of the matrix so that the columns become rows in reverse order. This operation is commonly used in image processing, graphics, and various algorithms that involve matrix transformations.

![Rotate 2d Matrix](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9W4RYNl70kBIaUw90ajJC3lu_dEIl9arSDg&usqp=CAU)

## Algorithm

To rotate an n x n 2D matrix by 90 degrees clockwise, you can follow these steps:

1. **Transpose the Matrix**: Swap elements across the main diagonal (from top-left to bottom-right). This step effectively converts rows into columns and columns into rows without altering the order of elements along the diagonal.

2. **Reverse Each Row**: After transposing, reverse the elements in each row. This step ensures that the columns, which have now become rows, are arranged in reverse order.

## Implementation

Here's a Python implementation of the algorithm:

```python
def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

## Example

Consider the following 3x3 matrix as an example:

```
1  2  3
4  5  6
7  8  9
```

After applying the `rotate_2d_matrix` function, the matrix will be rotated by 90 degrees clockwise:

```
7  4  1
8  5  2
9  6  3
```

## Usage

You can use the provided implementation in your code as follows:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

Running this code will output the rotated matrix:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

This demonstrates how the algorithm works and how you can use it to rotate a 2D matrix by 90 degrees clockwise.
