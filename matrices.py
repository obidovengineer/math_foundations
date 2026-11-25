# MATRICES (not just copied and pasted I wrote after understanding all the codes)

from __future__ import annotations
import vectors

class Matrix:
    def __init__(self, rows: list[list[int | float]]) -> None:
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))

    def __matmul__(self, other: Matrix) -> Matrix:
        if isinstance(other, vectors.Vector):
            if self.shape[1] == other.dimension:
                return vectors.Vector([
                    sum(self.rows[i][j] * other.components[j] for j in range(self.shape[1]))
                    for i in range(self.shape[0])
                ])
            else:
                raise ValueError("In order to complete this operation num of cols of a matrix should be equal to the num of rows of a vector.")

        if self.shape[1] == other.shape[0]:
            rows = []
            for i in range(self.shape[0]): 
                row = []
                for j in range(other.shape[1]):
                    row.append(sum(
                        self.rows[i][k] * other.rows[k][j]
                        for k in range(self.shape[1]) 
                    ))
                rows.append(row)
            return Matrix(rows)
        else:
            raise ValueError("In order to complete this operation num of cols of a first matrix should be equal to the num of rows of a second matrix.")

    def transpose(self) -> Matrix:
        return Matrix([
            [self.rows[j][i] for j in range(self.shape[0])]
            for i in range(self.shape[1])
        ])

    def __repr__(self) -> str:
        return f"Matrix({self.rows})"


if __name__ == "__main__":
    rotate_90_degs = Matrix([[0, -1], [1, 0]])
    point = vectors.Vector([3, 1])

    rotated_point = rotate_90_degs @ point

    print(f"Original: {point}")
    print(f"Rotated 90 degrees: {rotated_point}")