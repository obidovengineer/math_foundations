# Linear independence and projection from scratch using pure python

import vectors
import matrices


# it was a little bit difficult to understand this function although I know how to find RREF on paper
def is_linearly_independent(vectors: list[vectors.Vector]) -> bool:
    n = len(vectors)
    dim = len(vectors[0].components)
    mat = matrices.Matrix([v.components[:] for v in vectors])
    rows = [row[:] for row in mat.rows]
    rank = 0

    for col in range(dim):
        pivot = None

        for row in range(rank, len(rows)):
            if abs(rows[row][col]) > 1e-10:
                pivot = row
                break

        if pivot is None:
            continue

        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [x / scale for x in rows[rank]]

        for row in range(len(rows)):
            if row != rank and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col]
                rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]
        rank += 1

    return rank == n 

def project(a: vectors.Vector, b: vectors.Vector) -> vectors.Vector:
    scalar = a.dot(b) / b.dot(b)
    return vectors.Vector([scalar * x for x in b.components])

def gram_schmidt(vectors: list[vectors.Vector]) -> list[vectors.Vector]:
    orthonormal = []

    for v in vectors:
        w = v
        for u in orthonormal:
            proj = project(w, u)
            w = w - proj
        if w.magnitude() < 1e-10:
            continue
        orthonormal.append(w.normalize())
    return orthonormal

v1 = vectors.Vector([1, 0, 0])
v2 = vectors.Vector([1, 1, 0])
v3 = vectors.Vector([1, 1, 1])

basis = gram_schmidt([v1, v2, v3])

for i, u in enumerate(basis):
    print(f"u{i+1} = {u}")
    print(f"  |u{i+1}| = {u.magnitude():.6f}")

print(f"\nu1 · u2 = {basis[0].dot(basis[1]):.6f}")
print(f"u1 · u3 = {basis[0].dot(basis[2]):.6f}")
print(f"u2 · u3 = {basis[1].dot(basis[2]):.6f}")