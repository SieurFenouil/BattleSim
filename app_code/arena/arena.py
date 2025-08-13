# todo
# This is everything combat
# entities, combat, etc.

#todo next - set up combat teams
#todo - set some of those fcts as ArenaEnv class methds

import random

from app_code.barracks import barracks

class CombatEntity:
  def __init__(self, template):
    self.template : barracks.FighterTemplate = template
    self.team : CombatTeam = CombatTeam()
    self.alive : bool = True
    self.current_hp : int = self.template.max_hp
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

class ArenaEnv:
  def __init__(self):
    self.combat_teams : list[CombatTeam] = []
    self.biome : str = "0"


  def setup_battle(self):
    unit1 = CombatEntity(barracks.template_list[0])
    team1 = CombatTeam()
    team1.unit_list = [unit1]
    self.combat_teams = [team1]

  def fight_battle(self):

    battle_setlist = [ team for team in self.combat_teams]

    battle_over = False

    if len(battle_setlist) == 1 :
      battle_over = True
      print("battle over !")
      return battle_over

    else :
      turn_setlist = []
      surviving_units = []

      for team in battle_setlist :
        for unit in team.unit_list :

          unit.speed_meter += unit.template.speed * 0.05
          if unit.speed_meter >= 100 :
            turn_setlist.append(unit)

      speed_sort(turn_setlist)

      for unit in turn_setlist :

        # could have been killed by a previous unit in the turn_setlist
        if unit.current_hp > 0 :

        # pick targets, do actions

          target_list = [ target for team in battle_setlist if team != unit.team for target in team.unit_list]

          target = random.choice(target_list)

          target.current_hp -= unit.attack()
          if target.current_hp <= 0 :
            target.alive = False

          unit.speed_meter = 0

      surviving_units = [unit for team in battle_setlist for unit in team.unit_list if unit.current_hp > 0]

      for team in battle_setlist :
        team.unit_list = [unit for unit in surviving_units if unit.team == team]

      battle_setlist = [ team for team in battle_setlist if team.unit_list != []]

      return battle_over




######### functions ###################

###
def speed_sort(unit_list : list[CombatEntity]) :
  unit_list.sort(key=lambda x: x.speed_meter, reverse=True)

###
def setup_battle(team1 : CombatTeam, team2 : CombatTeam):
    print("nothing here yet")
