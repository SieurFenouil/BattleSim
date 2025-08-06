"""
Unit definitions and management.
Contains unit classes and related functionality.
"""

from typing import Dict, Any
import random


class Unit:
    """
    Represents a battle unit with stats and abilities.
    """
    
    def __init__(self, name: str, health: int, attack: int, defense: int, 
                 unit_type: str = "Basic", rarity: str = "Common"):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.attack = attack
        self.defense = defense
        self.unit_type = unit_type
        self.rarity = rarity
        self.level = 1
    
    def get_info(self) -> str:
        """Get detailed information about the unit."""
        status = "Healthy" if self.current_health == self.max_health else f"{self.current_health}/{self.max_health} HP"
        return (f"{self.name} (Lv.{self.level}) - {self.rarity} {self.unit_type}\n"
                f"  HP: {self.current_health}/{self.max_health} | ATK: {self.attack} | DEF: {self.defense}\n"
                f"  Status: {status}")
    
    def get_short_info(self) -> str:
        """Get brief information about the unit."""
        return f"{self.name} ({self.current_health}/{self.max_health})"
    
    def take_damage(self, damage: int) -> int:
        """Apply damage to the unit and return actual damage taken."""
        actual_damage = max(0, damage - self.defense)
        self.current_health = max(0, self.current_health - actual_damage)
        return actual_damage
    
    def heal(self, amount: int):
        """Heal the unit by the specified amount."""
        self.current_health = min(self.max_health, self.current_health + amount)
    
    def is_alive(self) -> bool:
        """Check if the unit is still alive."""
        return self.current_health > 0
    
    def level_up(self):
        """Level up the unit, increasing its stats."""
        self.level += 1
        
        # Increase stats by a small amount
        health_gain = random.randint(5, 15)
        attack_gain = random.randint(1, 3)
        defense_gain = random.randint(1, 2)
        
        self.max_health += health_gain
        self.current_health += health_gain
        self.attack += attack_gain
        self.defense += defense_gain
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert unit to dictionary for serialization."""
        return {
            'name': self.name,
            'max_health': self.max_health,
            'current_health': self.current_health,
            'attack': self.attack,
            'defense': self.defense,
            'unit_type': self.unit_type,
            'rarity': self.rarity,
            'level': self.level
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Unit':
        """Create unit from dictionary."""
        unit = cls(
            name=data['name'],
            health=data['max_health'],
            attack=data['attack'],
            defense=data['defense'],
            unit_type=data.get('unit_type', 'Basic'),
            rarity=data.get('rarity', 'Common')
        )
        unit.current_health = data['current_health']
        unit.level = data.get('level', 1)
        return unit


class UnitFactory:
    """
    Factory class for creating predefined units.
    """
    
    UNIT_TEMPLATES = {
        'warrior': {
            'name': 'Warrior',
            'health': 100,
            'attack': 20,
            'defense': 15,
            'unit_type': 'Fighter',
            'rarity': 'Common'
        },
        'archer': {
            'name': 'Archer',
            'health': 70,
            'attack': 25,
            'defense': 8,
            'unit_type': 'Ranged',
            'rarity': 'Common'
        },
        'mage': {
            'name': 'Mage',
            'health': 60,
            'attack': 30,
            'defense': 5,
            'unit_type': 'Caster',
            'rarity': 'Uncommon'
        },
        'knight': {
            'name': 'Knight',
            'health': 120,
            'attack': 18,
            'defense': 20,
            'unit_type': 'Tank',
            'rarity': 'Rare'
        }
    }
    
    @classmethod
    def create_unit(cls, unit_key: str) -> Unit:
        """Create a unit from a template."""
        if unit_key not in cls.UNIT_TEMPLATES:
            raise ValueError(f"Unknown unit type: {unit_key}")
        
        template = cls.UNIT_TEMPLATES[unit_key]
        return Unit(**template)
    
    @classmethod
    def create_random_unit(cls) -> Unit:
        """Create a random unit from available templates."""
        unit_key = random.choice(list(cls.UNIT_TEMPLATES.keys()))
        return cls.create_unit(unit_key)
    
    @classmethod
    def get_available_units(cls) -> list:
        """Get list of available unit types."""
        return list(cls.UNIT_TEMPLATES.keys())
