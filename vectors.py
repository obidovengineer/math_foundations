# VECTORS (wrote from scratch to understand how all the operations work)

from __future__ import annotations
from math import sqrt


class Vector:
    def __init__(self, components: list[int | float]) -> None:
        self.components = list(components)
        self.dimension = len(self.components)

    def __add__(self, other: Vector) -> Vector:
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other: Vector) -> Vector:
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self, other: Vector) -> int | float:
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self) -> float:
        return sqrt(sum(x**2 for x in self.components))

    def normalize(self) -> Vector:
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector([x / mag for x in self.components])

    def cosine_similarity(self, other: Vector) -> float:
        denominator = self.magnitude() * other.magnitude()
        if denominator == 0:
            raise ValueError("Cosine similarity is undefined for zero vectors")
        return self.dot(other) / denominator

    def __repr__(self) -> str:
        return f"Vector({self.components})"

a = Vector([1, 2, 3])
b = Vector([4, 5, 6])

print(f"a + b = {a + b}")
print(f"a * b = {a.dot(b)}") 
print(f"|a| = {a.magnitude():.4f}")
print(f"cosine similarity = {a.cosine_similarity(b):.4f}")