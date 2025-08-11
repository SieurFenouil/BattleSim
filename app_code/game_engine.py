from game_state import GameState

class GameEngine():
  def __init__(self):
    self.input_array = []
    self.display_array = []
    self.game_state = None

  def init(self):
    self.game_state = GameState()
    self.game_state.init()

  def check_inputs(self):
    print("check inputs")
    #nothing yet

  def update_game_state(self):
    print("update game state")
    #nothing yet

  def refresh_display(self):
    print("refresh display")
    #nothing yet