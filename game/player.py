"""
Player class and related functionality.
Manages player state, progress, and team.
"""

from typing import List, Dict, Any
from game.units import Unit, UnitFactory


class Player:
    """
    Represents the player with their progress and team.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.experience = 0
        self.gold = 100
        self.wins = 0
        self.losses = 0
        self.team: List[Unit] = []
        
        # Initialize with a starting unit
        self.add_starting_units()
    
    def add_starting_units(self):
        """Add starting units to the player's team."""
        # Give player a basic warrior to start with
        starter_unit = UnitFactory.create_unit('warrior')
        self.team.append(starter_unit)
    
    def add_unit(self, unit: Unit) -> bool:
        """
        Add a unit to the player's team.
        Returns True if successful, False if team is full.
        """
        max_team_size = 5  # Maximum team size
        
        if len(self.team) < max_team_size:
            self.team.append(unit)
            return True
        else:
            return False
    
    def remove_unit(self, index: int) -> bool:
        """
        Remove a unit from the team by index.
        Returns True if successful, False if invalid index.
        """
        if 0 <= index < len(self.team):
            self.team.pop(index)
            return True
        else:
            return False
    
    def level_up(self):
        """Level up the player."""
        self.level += 1
        self.gold += 50  # Bonus gold for leveling up
        
        # Reset experience for next level
        experience_needed = self.level * 100
        self.experience -= experience_needed
    
    def add_experience(self, amount: int):
        """Add experience to the player."""
        self.experience += amount
        
        # Check for level up
        while self.experience >= self.level * 100:
            self.level_up()
    
    def add_gold(self, amount: int):
        """Add gold to the player."""
        self.gold += amount
    
    def spend_gold(self, amount: int) -> bool:
        """
        Spend gold if the player has enough.
        Returns True if successful, False if insufficient funds.
        """
        if self.gold >= amount:
            self.gold -= amount
            return True
        else:
            return False
    
    def get_win_rate(self) -> float:
        """Calculate the player's win rate."""
        total_games = self.wins + self.losses
        if total_games == 0:
            return 0.0
        return (self.wins / total_games) * 100
    
    def display_status(self):
        """Display the player's current status."""
        print(f"\n=== {self.name.upper()}'S STATUS ===")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}/{self.level * 100}")
        print(f"Gold: {self.gold}")
        print(f"Record: {self.wins}W - {self.losses}L ({self.get_win_rate():.1f}% win rate)")
        print(f"Team Size: {len(self.team)}/5")
        
        if self.team:
            print("\nCurrent Team:")
            for i, unit in enumerate(self.team, 1):
                print(f"  {i}. {unit.get_short_info()}")
        else:
            print("\nNo units in team!")
        print()
    
    def heal_all_units(self):
        """Heal all units in the team to full health."""
        for unit in self.team:
            unit.heal(unit.max_health)
    
    def get_team_power(self) -> int:
        """Calculate total power of the player's team."""
        total_power = 0
        for unit in self.team:
            power = unit.health + unit.attack + unit.defense
            total_power += power
        return total_power
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert player to dictionary for serialization."""
        return {
            'name': self.name,
            'level': self.level,
            'experience': self.experience,
            'gold': self.gold,
            'wins': self.wins,
            'losses': self.losses,
            'team': [unit.to_dict() for unit in self.team]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        """Create player from dictionary."""
        player = cls(data['name'])
        player.level = data['level']
        player.experience = data['experience']
        player.gold = data['gold']
        player.wins = data['wins']
        player.losses = data['losses']
        
        # Clear starting units and load saved team
        player.team = []
        for unit_data in data['team']:
            unit = Unit.from_dict(unit_data)
            player.team.append(unit)
        
        return player
