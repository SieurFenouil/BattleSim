# todo
# This is everything combat
# entities, combat, etc.

import random
import barracks

class CombatEntity:
  def __init__(self, template):
    self.template : barracks.FighterTemplate = template
    self.team : CombatTeam = CombatTeam()
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


def speed_sort(unit_list : list[CombatEntity]) :
  unit_list.sort(key=lambda x: x.speed_meter, reverse=True)

def fight_battle(team1 : CombatTeam, team2 : CombatTeam):

  battle_setlist = [ team1.unit_list, team2.unit_list]
  
  battle_over = False

  while(not battle_over):

    turn_setlist = []
    surviving_units = []

    for team in battle_setlist :
      for unit in team :
      
        unit.speed_meter += unit.template.speed * 0.05
        if unit.speed_meter >= 100 :
          turn_setlist.append(unit)

    speed_sort(turn_setlist)
    
    for unit in turn_setlist :

      target = CombatEntity(barracks.FighterTemplate("dummy"))
      # could have been killed by a previous unit in the turn_setlist
      if unit.current_hp > 0 :
        
      # pick targets, do actions

        target_list = [ target for team in battle_setlist if team != unit.team for target in team]

        target = random.choice(target_list)

        target.current_hp -= unit.attack()
      if target.current_hp <= 0 :
        target.alive = False
 
        unit.speed_meter = 0
    
    surviving_units = [unit for team in battle_setlist for unit in team if unit.current_hp > 0]

    for team in battle_setlist :
      team = [unit for unit in surviving_units if unit.team == team]

    battle_setlist = [ team for team in battle_setlist if team != []]

    if len(battle_setlist) == 1 :
      battle_over = True
      return battle_setlist[0]
    