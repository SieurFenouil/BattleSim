"""
Battle system and combat mechanics.
Handles battle simulation and combat logic.
"""

import random
import time
from typing import List, Optional

from game.units import Unit
from utils.console import Console


class BattleManager:
    """
    Manages battle simulation and combat mechanics.
    """
    
    def __init__(self):
        self.battle_log: List[str] = []
    
    def simulate_battle(self, player) -> bool:
        """
        Simulate a battle for the player.
        Returns True if player wins, False if player loses.
        """
        self.battle_log.clear()
        
        Console.print_info("Preparing for battle...")
        time.sleep(1)
        
        # Create enemy team (placeholder)
        enemy_team = self.generate_enemy_team()
        
        Console.print_info("Battle begins!")
        self.display_teams(player.team, enemy_team, "Your Team", "Enemy Team")
        
        # Simple battle simulation
        player_power = self.calculate_team_power(player.team)
        enemy_power = self.calculate_team_power(enemy_team)
        
        Console.print_info(f"Your team power: {player_power}")
        Console.print_info(f"Enemy team power: {enemy_power}")
        
        # Add some randomness to the battle
        player_roll = player_power + random.randint(1, 20)
        enemy_roll = enemy_power + random.randint(1, 20)
        
        Console.print_info("Battle in progress...")
        time.sleep(2)
        
        # Simulate battle rounds
        self.simulate_battle_rounds(player.team, enemy_team)
        
        # Determine winner
        victory = player_roll > enemy_roll
        
        if victory:
            Console.print_success(f"Victory! (Your roll: {player_roll} vs Enemy: {enemy_roll})")
            player.experience += 10
        else:
            Console.print_error(f"Defeat! (Your roll: {player_roll} vs Enemy: {enemy_roll})")
            player.experience += 5
        
        # Check for level up
        if player.experience >= player.level * 100:
            player.level_up()
            Console.print_success("Level up!")
        
        input("Press Enter to continue...")
        return victory
    
    def generate_enemy_team(self) -> List[Unit]:
        """Generate a random enemy team."""
        enemy_team = []
        team_size = random.randint(1, 3)
        
        enemy_names = ["Goblin", "Orc", "Skeleton", "Spider", "Wolf"]
        
        for i in range(team_size):
            name = random.choice(enemy_names)
            health = random.randint(50, 100)
            attack = random.randint(10, 25)
            defense = random.randint(5, 15)
            
            unit = Unit(name, health, attack, defense)
            enemy_team.append(unit)
        
        return enemy_team
    
    def calculate_team_power(self, team: List[Unit]) -> int:
        """Calculate total power of a team."""
        if not team:
            return 10  # Minimum power for empty team
        
        total_power = 0
        for unit in team:
            power = unit.health + unit.attack + unit.defense
            total_power += power
        
        return total_power
    
    def display_teams(self, player_team: List[Unit], enemy_team: List[Unit], 
                     player_label: str = "Player", enemy_label: str = "Enemy"):
        """Display both teams side by side."""
        print(f"\n{player_label:20} | {enemy_label}")
        print("-" * 40)
        
        max_size = max(len(player_team), len(enemy_team))
        
        for i in range(max_size):
            player_unit = player_team[i] if i < len(player_team) else None
            enemy_unit = enemy_team[i] if i < len(enemy_team) else None
            
            player_str = player_unit.get_short_info() if player_unit else ""
            enemy_str = enemy_unit.get_short_info() if enemy_unit else ""
            
            print(f"{player_str:20} | {enemy_str}")
        
        print()
    
    def simulate_battle_rounds(self, player_team: List[Unit], enemy_team: List[Unit]):
        """Simulate individual battle rounds (placeholder)."""
        rounds = random.randint(3, 6)
        
        for round_num in range(1, rounds + 1):
            Console.print_info(f"Round {round_num}...")
            time.sleep(0.5)
            
            # Simple round simulation
            if player_team and enemy_team:
                player_unit = random.choice(player_team)
                enemy_unit = random.choice(enemy_team)
                
                damage = max(1, player_unit.attack - enemy_unit.defense + random.randint(-5, 5))
                
                action_text = f"{player_unit.name} attacks {enemy_unit.name} for {damage} damage!"
                print(f"  {action_text}")
                self.battle_log.append(action_text)
        
        Console.print_info("Battle concluded!")
    
    def get_battle_log(self) -> List[str]:
        """Get the current battle log."""
        return self.battle_log.copy()
