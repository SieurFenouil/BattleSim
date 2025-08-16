from enum import Enum
from .arena.arena import ArenaEnv

class GameStateEnum(Enum):
    SETUP = 0           # barracks stuff ? team creation, level ups, all that
    BATTLE = 1          # this is a battle
    BATTLE_OVER = 2     # this is a battle finished

class GameState():
  def __init__(self):
    self.state = None
    self.arena_env = None

  def init(self):
    self.state = GameStateEnum.SETUP
    self.arena_env = ArenaEnv()

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
            if(command == 0x0000):
              self.state = GameStateEnum.SETUP
