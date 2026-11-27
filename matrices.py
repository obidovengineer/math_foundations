# MATRICES (not just copied and pasted I wrote after understanding all the codes)

from __future__ import annotations
import vectors

class Matrix:
    def __init__(self, rows: list[list[int | float]]) -> None:
        self.rows = [list(row) for row in rows]
        self.shape = (len(self.rows), len(self.rows[0]))

    def __add__(self, other: Matrix) -> Matrix:
        return Matrix([
            [self.rows[i][j] + other.rows[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ])

    def __sub__(self, other: Matrix) -> Matrix:
        return Matrix([
            [self.rows[i][j] - other.rows[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ])

    def scalar_multiply(self, scalar: int | float) -> Matrix:
        return Matrix([
            [scalar * self.rows[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ])

    def element_wise_multiply(self, other: Matrix) -> Matrix:
        return Matrix([
            [self.rows[i][j] * other.rows[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ])

    def determinant(self) -> int | float:
        if self.shape == (1, 1):
            return self.rows[0][0]
        if self.shape == (2, 2):
            return (self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1, 0])

        det = 0 
        for j in range(self.shape[1]):
            minor = Matrix([
                [self.rows[i][k] for k in range(self.shape[1]) if k != j]
                for i in range(1, self.shape[0])
            ])
            det += ((-1) ** j) * self.rows[0][j] * minor.determinant()

        return det

    def inverse_2x2(self) -> Matrix:
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular, no inverse exists")
        return Matrix([
            [self.rows[1][1] / det, -self.rows[0][1] / det],
            [-self.rows[1][0] / det, self.rows[0][0] / det]
        ])

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
        row_str = "\n  ".join(str(row) for row in self.rows)
        return f"Matrix({self.shape}):\n  {row_str}"

    @staticmethod
    def identity(n: int) -> Matrix:
        return Matrix([
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ])


if __name__ == "__main__":
    rotate_90_degs = Matrix([[0, -1], [1, 0]])
    point = vectors.Vector([3, 1])

    rotated_point = rotate_90_degs @ point

    print(f"Original: {point}")
    print(f"Rotated 90 degrees: {rotated_point}")