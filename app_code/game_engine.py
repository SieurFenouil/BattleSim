from .game_state import GameState
from .hmi import Hmi

from enum import Enum

class EngineStatusEnum(Enum):
    FAILED = 0
    STOPPED = 1
    INIT = 2
    RUNNING = 3
    
class GameEngine():
  def __init__(self):
    self.status = EngineStatusEnum.FAILED
    self.display_array = []
    self.hmi = None
    self.game_state = None

  def init(self):
    self.status = EngineStatusEnum.RUNNING
    self.hmi = Hmi()
    self.hmi.init()
    self.game_state = GameState()
    self.game_state.init()

  def request_inputs(self):
    print("request inputs")
    self.hmi.request_inputs(self.game_state.state)

  def update_game_state(self):
    print("update game state")
    self.game_state.process_state_machine(self.hmi.last_command)

  def refresh_display(self):
    print("refresh display")
    #nothing yet