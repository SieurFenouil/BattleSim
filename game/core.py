"""
Core game management and main game loop.
Handles the primary game flow and state management.
"""

import time
from typing import Optional

from game.player import Player
from game.battle import BattleManager
from utils.console import Console
from utils.input_handler import InputHandler


class GameState:
    """Enumeration for different game states."""
    MENU = "menu"
    PREPARATION = "preparation"
    BATTLE = "battle"
    SHOP = "shop"
    RESULTS = "results"
    GAME_OVER = "game_over"


class GameManager:
    """
    Main game manager that handles the overall game flow and state.
    """
    
    def __init__(self):
        self.player: Optional[Player] = None
        self.battle_manager = BattleManager()
        self.input_handler = InputHandler()
        self.current_state = GameState.MENU
        self.round_number = 1
        self.running = False
    
    def start_new_game(self):
        """Initialize and start a new game."""
        try:
            Console.print_info("Initializing new game...")
            
            # Create player
            player_name = self.input_handler.get_string_input("Enter your name: ")
            self.player = Player(player_name)
            
            Console.print_success(f"Welcome, {player_name}!")
            self.current_state = GameState.PREPARATION
            self.running = True
            
            # Start main game loop
            self.game_loop()
            
        except Exception as e:
            Console.print_error(f"Failed to start new game: {e}")
            self.input_handler.wait_for_enter()
    
    def game_loop(self):
        """Main game loop that handles different game states."""
        while self.running:
            try:
                if self.current_state == GameState.PREPARATION:
                    self.handle_preparation_phase()
                elif self.current_state == GameState.BATTLE:
                    self.handle_battle_phase()
                elif self.current_state == GameState.SHOP:
                    self.handle_shop_phase()
                elif self.current_state == GameState.RESULTS:
                    self.handle_results_phase()
                elif self.current_state == GameState.GAME_OVER:
                    self.handle_game_over()
                    break
                else:
                    Console.print_error(f"Unknown game state: {self.current_state}")
                    break
                    
            except KeyboardInterrupt:
                Console.print_info("\nReturning to main menu...")
                break
            except Exception as e:
                Console.print_error(f"Error in game loop: {e}")
                self.input_handler.wait_for_enter()
    
    def handle_preparation_phase(self):
        """Handle the preparation phase before battle."""
        Console.clear()
        Console.print_header(f"=== ROUND {self.round_number} - PREPARATION ===")
        
        if self.player:
            self.player.display_status()
        
        print("\nPreparation Phase:")
        print("1. View Team")
        print("2. Start Battle")
        print("3. Return to Main Menu")
        
        choice = self.input_handler.get_menu_choice("Choose action (1-3): ", 1, 3)
        
        if choice == 1:
            self.show_team_info()
        elif choice == 2:
            self.current_state = GameState.BATTLE
        elif choice == 3:
            self.running = False
    
    def handle_battle_phase(self):
        """Handle the battle phase."""
        Console.clear()
        Console.print_header(f"=== ROUND {self.round_number} - BATTLE ===")
        
        if self.player:
            battle_result = self.battle_manager.simulate_battle(self.player)
            
            if battle_result:
                Console.print_success("Victory!")
                self.player.wins += 1
            else:
                Console.print_error("Defeat!")
                self.player.losses += 1
            
            self.current_state = GameState.RESULTS
        else:
            Console.print_error("No player found!")
            self.current_state = GameState.GAME_OVER
    
    def handle_shop_phase(self):
        """Handle the shop phase (placeholder)."""
        Console.print_info("Shop phase not implemented yet.")
        self.input_handler.wait_for_enter()
        self.current_state = GameState.PREPARATION
    
    def handle_results_phase(self):
        """Handle the results phase after battle."""
        Console.print_header("=== BATTLE RESULTS ===")
        
        if self.player:
            self.player.display_status()
        
        print("\nWhat would you like to do?")
        print("1. Continue to next round")
        print("2. Return to main menu")
        
        choice = self.input_handler.get_menu_choice("Choose (1-2): ", 1, 2)
        
        if choice == 1:
            self.round_number += 1
            self.current_state = GameState.PREPARATION
        else:
            self.running = False
    
    def handle_game_over(self):
        """Handle game over state."""
        Console.print_header("=== GAME OVER ===")
        
        if self.player:
            print(f"Final Stats for {self.player.name}:")
            self.player.display_status()
        
        self.input_handler.wait_for_enter()
        self.running = False
    
    def show_team_info(self):
        """Display information about the player's team."""
        Console.clear()
        Console.print_header("=== YOUR TEAM ===")
        
        if self.player and self.player.team:
            for i, unit in enumerate(self.player.team, 1):
                print(f"{i}. {unit.get_info()}")
        else:
            Console.print_info("No units in your team yet.")
        
        self.input_handler.wait_for_enter()
