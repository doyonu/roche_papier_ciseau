from enum import Enum

class GameState(Enum):
    NOT_STARTED = False
    ROUND_ACTIVE = False
    ROUND_DONE = False
    GAME_OVER = False