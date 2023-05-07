from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tic_tac_toe.logic.models import GameState, Grid

import re

def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")
    
def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(
        game_state.grid, game_state.starting_mark, game_state.winner
    )