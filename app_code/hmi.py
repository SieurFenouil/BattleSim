from .game_state import GameStateEnum

class Hmi():
  def __init__(self):
    self.last_command = None

  def init(self):
    print("init hmi")

  def request_inputs(self,state):

    self.last_command = 0x0000

    match(state):
      case GameStateEnum.BATTLE_OVER:
        input_str = input("press y to continue \n")
        if (input_str == "y"):
          print("you pressed y")
          self.last_command = 0x0001
