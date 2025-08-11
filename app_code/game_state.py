from enum import Enum

class GameStateEnum(Enum):
    SETUP = 0
    BATTLE = 1

class GameState():
  def __init__(self):
    self.state = None

  def init(self):
    self.state = GameStateEnum.SETUP