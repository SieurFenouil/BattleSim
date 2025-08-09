# todo
# This is everything combat
# entities, combat, etc.

import random
import barracks

class CombatEntity:
  def __init__(self, template):
    self.template : barracks.FighterTemplate = template
    self.team : int = 0
    self.alive : bool = True
    self.currentHP : int = 0
    self.speedMeter : float = 0

  def attack(self):

    # add parry, dodge, block, combo, retaliate
    return self.template.strength

# combat teams set up in barracks or arena level ?
class CombatTeam:
  def __init__(self):
    self.unitList : list[CombatEntity] =[]

  def addUnit(self, unit):
    self.unitList.append(unit)


def speed_sort(unitList : list[CombatEntity])
  unitList.sort(key=lambda x: x.speedMeter, reverse=True)

def fight_battle(Team1 : CombatTeam, Team2 : CombatTeam):

  UnitList = Team1.unitList + Team2.unitList
  
  battle_over = False

  while(not battle_over):

    UnitsPlayingThisTurn = []

    for unit in UnitList :
      unit.speedMeter += unit.template.speed * 0.05
      if unit.speedMeter >= 100 :
        UnitsPlayingThisTurn.append(unit)

    speed_sort(UnitsPlayingThisTurn)
    
    for unit in UnitsPlayingThisTurn :

      # pick targets, do actions

      if unit.team == 1 :
        target = random.randint(0, len(Team2.unitList) - 1)
        unit.attack(
          Team2.unitList[target])

      if unit.team == 2 :
        target = random.randint(0, len(Team1.unitList) - 1)
        unit.attack(
          Team1.unitList[target])