# Todo :
# This is everything outside of combat
# Fighter creation, template, level up,
# skills, weapons, items, etc.

import random

from app_code.barracks.generic_classes import GenericTemplate
from app_code.barracks.generic_classes import Saveable

class FighterTemplate(GenericTemplate, Saveable):
  def __init__(self):
    super().__init__()
    self.strength : int = 0
    self.agility : int = 0
    self.speed : int = 0
    self.max_hp : int = 0

  #TODO init from a standard const array declared elsewhere rather than magic numbers here
  def init(self, name : str):
    super().init(name)
    self.strength : int = 1
    self.agility : int = 1
    self.speed : int = 1
    self.max_hp : int = 40


  def create_fighter(self):
    upgrades_pool = 10 #TODO Magic numbers

    for i in range(upgrades_pool):
      stat = random.randint(1, 5)
      if stat == 1:
        self.strength += 1
      elif stat == 2:
        self.agility += 1
      elif stat == 3:
        self.speed += 1
      elif (stat == 4 or stat == 5):
        self.max_hp += 10