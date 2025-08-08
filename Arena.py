# todo
# This is everything combat
# entities, combat, etc.

import barracks

class CombatEntity:
  def __init__(self, template, team):
    self.template : barracks.FighterTemplate = template
    self.team : int = team
    self.alive : bool = True
    self.currentHP : int = 0
    self.speedMeter : int = 0

  def attack(self):

    # add parry, dodge, block, combo, retaliate
    return self.template.strength

def fight_battle(brute1, brute2):

  # Do 1 list of lists, each sublist is a team
  UnitList = []
  Team1List = []
  Team2List = []

  Unit1 = CombatEntity(brute1, 1)
  UnitList.append(Unit1)
  Team1List.append(Unit1)

  Unit2 = CombatEntity(brute2, 2)
  UnitList.append(Unit2)
  Team2List.append(Unit2)

  battle_over = False

  while(battle_over == True):

    UnitsPlayingThisTurn = []

    for unit in UnitList :
      unit.speedMeter += unit.template.speed * 0.05
      if unit.speedMeter >= 100 :
        UnitsPlayingThisTurn.append(unit)

    # Need to sort this list by speed meter values first
    for unit in UnitsPlayingThisTurn :

      # pick targets, do actions

      if unit.team == team1 :
        unit.attack(Team2[0]) # should actually pick target

      if unit.team == team2 :
        unit.attack(Team1[0])

