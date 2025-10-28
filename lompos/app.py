"""Minimal FastAPI application exposing the Lompos puzzle models."""
from __future__ import annotations

from fastapi import FastAPI

from .models import Board, Piece, PuzzleDefinition

app = FastAPI(title="Lompos Cosmic Creature Helper")


@app.get("/board", response_model=Board)
def get_board() -> Board:
    """Return the board configuration for the puzzle."""
    return PuzzleDefinition.empty().board


@app.get("/pieces", response_model=list[Piece])
def list_pieces() -> list[Piece]:
    """Return the current set of pieces (empty until defined)."""
    return PuzzleDefinition.empty().pieces
