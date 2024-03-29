from __future__ import annotations
from . import algorithms

__all__ = ["Highlight", "algorithms"]

class Highlight:
    def to_tuple(self) -> tuple[int, int, float]: ...
    @property
    def data_index(self) -> int: ...
    @property
    def furthest_data_index(self) -> int: ...
    @property
    def max_distance(self) -> float: ...
