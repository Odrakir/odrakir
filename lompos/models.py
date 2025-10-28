"""Domain models for the Lompos Cosmic Creature puzzle."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Set, Tuple

Coordinate = Tuple[int, int]


@dataclass(frozen=True)
class Piece:
    """Represents a single Lompos puzzle piece.

    Attributes:
        name: Human friendly identifier for the piece.
        color: Color of the piece used by the puzzle.
        cells: Set of square coordinates occupied by the piece relative to its
            origin. The origin (0, 0) corresponds to the top-left square of the
            piece in its default orientation.
    """

    name: str
    color: str
    cells: Set[Coordinate]

    def normalized(self) -> "Piece":
        """Return a copy of the piece translated so the minimum coordinate is at the origin."""
        if not self.cells:
            return self

        min_x = min(x for x, _ in self.cells)
        min_y = min(y for _, y in self.cells)
        normalized_cells = {(x - min_x, y - min_y) for x, y in self.cells}
        return Piece(name=self.name, color=self.color, cells=normalized_cells)


@dataclass
class Board:
    """Represents the Lompos puzzle board.

    The board is 20 columns by 14 rows, but some edge cells are missing. Missing
    cells are stored as coordinates relative to the top-left corner of the
    nominal rectangle. Only valid coordinates that exist on the board should be
    tracked.
    """

    width: int = 20
    height: int = 14
    missing_cells: Set[Coordinate] = field(default_factory=set)

    def contains(self, coordinate: Coordinate) -> bool:
        """Return True if the coordinate exists on the board."""
        x, y = coordinate
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        return coordinate not in self.missing_cells

    def add_missing_cells(self, cells: Iterable[Coordinate]) -> None:
        """Mark multiple coordinates as missing from the board."""
        for cell in cells:
            x, y = cell
            if not (0 <= x < self.width and 0 <= y < self.height):
                raise ValueError(f"Coordinate {cell} lies outside of the board bounds")
            self.missing_cells.add(cell)


@dataclass
class PuzzleDefinition:
    """Holds the board and all puzzle pieces."""

    board: Board
    pieces: List[Piece]

    @classmethod
    def empty(cls) -> "PuzzleDefinition":
        """Return an empty puzzle definition with only board dimensions."""
        return cls(board=Board(), pieces=[])

    def piece_by_name(self, name: str) -> Piece:
        """Return the piece with the provided name."""
        for piece in self.pieces:
            if piece.name == name:
                return piece
        raise KeyError(f"No piece named {name!r} exists in this puzzle definition")
