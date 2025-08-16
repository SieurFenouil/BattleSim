from .game_state import GameStateEnum

class Hmi():
  def __init__(self):
    self.last_command = None

  def init(self):
    print("init hmi")

  def request_inputs(self,state):

    match(state):
      case GameStateEnum.BATTLE_OVER:
        input_str = input("press y to continue")
        if (input_str == "y"):
          self.last_command = 0x0000

