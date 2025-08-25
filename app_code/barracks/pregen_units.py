
from app_code.barracks.barracks import FighterTemplate

PREGEN_UNIT_DB = {}

def get_pregen_unit_database()  -> dict[str, FighterTemplate]:
  
  return PREGEN_UNIT_DB

goblin = FighterTemplate("Goblin")
goblin.strength = 1
goblin.agility = 4
goblin.speed = 5
goblin.max_hp = 40

PREGEN_UNIT_DB[goblin.name] = goblin

bandit = FighterTemplate("Bandit")
bandit.strength = 3
bandit.agility = 2
bandit.speed = 2
bandit.max_hp = 60

PREGEN_UNIT_DB[bandit.name] = bandit

giant = FighterTemplate("Giant")
giant.strength = 15
giant.agility = 2
giant.speed = 3
giant.max_hp = 300

PREGEN_UNIT_DB[giant.name] = giant
