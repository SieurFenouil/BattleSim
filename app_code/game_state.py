from ._common_enums.common_enums import GameStateEnum
from ._common_enums.common_enums import PlayerCommands
from .arena.arena import ArenaEnv

class GameState():
  def __init__(self):
    self.state = None
    self.arena_env = None

  def init(self):
    self.state = GameStateEnum.SETUP
    self.arena_env = ArenaEnv()
    self.arena_env.init()

    print("init game state")

  def process_state_machine(self, command):

      # shitty transition just for now
      match self.state:
          case GameStateEnum.SETUP:
            print("prepare battle")
            self.arena_env.setup_battle()
            self.state = GameStateEnum.BATTLE

      # battle state just for now
          case GameStateEnum.BATTLE:
            print("doing battle !")
            if(self.arena_env.fight_battle()):
              self.state = GameStateEnum.BATTLE_OVER

          case GameStateEnum.BATTLE_OVER:
            if(command == PlayerCommands.BACK_TO_SETUP):
              self.state = GameStateEnum.SETUP
