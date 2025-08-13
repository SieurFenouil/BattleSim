from .game_state import GameState
from .game_state import GameStateEnum

from enum import Enum

class EngineStatusEnum(Enum):
    FAILED = 0
    STOPPED = 1
    INIT = 2
    RUNNING = 3
    
class GameEngine():
  def __init__(self):
    self.status = EngineStatusEnum.FAILED
    self.input_array = []
    self.display_array = []
    self.game_state = None

  def init(self):
    self.status = EngineStatusEnum.RUNNING
    self.game_state = GameState()
    self.game_state.init()

  def check_inputs(self):
    print("check inputs")
    #nothing yet

  def update_game_state(self):
    print("update game state")
    self.game_state.process_state_machine(self.input_array)
    if self.game_state.state == GameStateEnum.BATTLE_OVER :
      self.status = EngineStatusEnum.STOPPED

  def refresh_display(self):
    print("refresh display")
    #nothing yet