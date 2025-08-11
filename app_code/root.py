
from .game_engine import GameEngine

class Root :
  def __init__(self) :
    self.game = None

  def init(self) :
    print("init")
    self.game = GameEngine()
    self.game.init()
  
  def run(self) :
    while(1) :
      # check for inputs
      self.game.check_inputs()
      # update game state
      self.game.update_game_state()
      # refresh display
      self.game.refresh_display()