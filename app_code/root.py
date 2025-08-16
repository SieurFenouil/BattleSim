
import time
from .game_engine import GameEngine
from .game_engine import EngineStatusEnum

class Root :
  def __init__(self) :
    self.game = None

  def init(self) :
    print("init")
    self.game = GameEngine()
    self.game.init()
  
  def run(self) :
    i = 0
    while(self.game.status == EngineStatusEnum.RUNNING) :
      print("\n loop : ", i, "\n")
      i+=1
      # check for inputs
      self.game.request_inputs()
      # update game state
      self.game.update_game_state()
      # refresh display
      self.game.refresh_display()

      time.sleep(0.5)