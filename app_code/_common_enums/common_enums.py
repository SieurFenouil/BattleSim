from enum import Enum

class GameStateEnum(Enum):
    SETUP = 0           # barracks stuff ? team creation, level ups, all that
    BATTLE = 1          # this is a battle
    BATTLE_OVER = 2     # this is a battle finished

class PlayerCommands(Enum):
   NONE = 0x0000
   BACK_TO_SETUP = 0x9000