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
    self.current_hp : int = 0
    self.speed_meter : float = 0

  def attack(self):

    # add parry, dodge, block, combo, retaliate
    return self.template.strength

# combat teams set up in barracks or arena level ?
class CombatTeam:
  def __init__(self):
    self.unit_list : list[CombatEntity] =[]

  def add_unit(self, unit):
    self.unit_list.append(unit)


def speed_sort(unitList : list[CombatEntity]) :
  unitList.sort(key=lambda x: x.speed_meter, reverse=True)

def fight_battle(Team1 : CombatTeam, Team2 : CombatTeam):

  battle_setlist = Team1.unit_list + Team2.unit_list
  
  battle_over = False

  while(not battle_over):

    turn_setlist = []

    for unit in battle_setlist :
      unit.speed_meter += unit.template.speed * 0.05
      if unit.speed_meter >= 100 :
        turn_setlist.append(unit)

    speed_sort(turn_setlist)
    
    for unit in turn_setlist :

      # pick targets, do actions

      if unit.team == 1 :
        target = random.randint(0, len(Team2.unit_list) - 1)
        unit.attack(
          Team2.unit_list[target])

      if unit.team == 2 :
        target = random.randint(0, len(Team1.unit_list) - 1)
        unit.attack(
          Team1.unit_list[target])