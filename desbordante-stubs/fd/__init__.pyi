from __future__ import annotations
import desbordante
from . import algorithms

__all__ = ["FD", "FdAlgorithm", "algorithms"]

class FD:
    def __eq__(self, arg0: FD) -> bool: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def to_index_tuple(self) -> tuple: ...
    def to_long_string(self) -> str: ...
    def to_name_tuple(self) -> tuple: ...
    def to_short_string(self) -> str: ...
    @property
    def lhs_indices(self) -> list[int]: ...
    @property
    def rhs_index(self) -> int: ...

class FdAlgorithm(desbordante.Algorithm):
    def get_fds(self) -> list[FD]: ...
