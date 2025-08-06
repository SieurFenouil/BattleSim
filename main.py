#!/usr/bin/env python3
"""
Auto Battler Game - Main Entry Point
A bare-bones console-based auto battler game foundation for future expansion.
"""

import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.console import Console
from utils.input_handler import InputHandler


def display_main_menu():
    """Display the main menu options."""
    Console.clear()
    Console.print_header("=== AUTO BATTLER ===")
    print("\n1. Start Game (Ready for your implementation)")
    print("2. Exit")
    print("\n" + "="*25)


def main():
    """Main entry point of the application."""
    Console.print_welcome()
    
    input_handler = InputHandler()
    
    try:
        while True:
            display_main_menu()
            
            choice = input_handler.get_menu_choice("Enter your choice (1-2): ", 1, 2)
            
            if choice == 1:
                # This is where you'll add your game logic
                Console.print_info("Game starting... (Add your implementation here)")
                Console.print_info("This is your development foundation!")
                input_handler.wait_for_enter()
            elif choice == 2:
                Console.print_info("Thanks for using the dev environment!")
                break
                
    except KeyboardInterrupt:
        Console.print_info("\nGame interrupted by user.")
    except Exception as e:
        Console.print_error(f"An unexpected error occurred: {e}")
    finally:
        Console.print_info("Goodbye!")


if __name__ == "__main__":
    main()
