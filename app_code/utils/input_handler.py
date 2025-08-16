"""
Input handling utilities for console applications.
Provides safe and validated input methods.
"""

import sys
from typing import Optional, List, Any


class InputHandler:
    """
    Handles user input with validation and error handling.
    """
    
    def __init__(self):
        self.input_history: List[str] = []
    
    def get_string_input(self, prompt: str, min_length: int = 1, 
                        max_length: int = 100, allow_empty: bool = False) -> str:
        """
        Get validated string input from user.
        
        Args:
            prompt: The input prompt to display
            min_length: Minimum length of input
            max_length: Maximum length of input
            allow_empty: Whether to allow empty input
            
        Returns:
            Validated string input
        """
        while True:
            try:
                user_input = input(prompt).strip()
                
                # Store in history
                if user_input:
                    self.input_history.append(user_input)
                
                if not user_input and not allow_empty:
                    print("Input cannot be empty. Please try again.")
                    continue
                
                if len(user_input) < min_length and not (allow_empty and not user_input):
                    print(f"Input must be at least {min_length} characters long.")
                    continue
                
                if len(user_input) > max_length:
                    print(f"Input must be no more than {max_length} characters long.")
                    continue
                
                return user_input
                
            except KeyboardInterrupt:
                print("\nInput cancelled.")
                raise
            except EOFError:
                print("\nEnd of input reached.")
                sys.exit(0)
    
    def get_integer_input(self, prompt: str, min_value: Optional[int] = None, 
                         max_value: Optional[int] = None) -> int:
        """
        Get validated integer input from user.
        
        Args:
            prompt: The input prompt to display
            min_value: Minimum allowed value
            max_value: Maximum allowed value
            
        Returns:
            Validated integer input
        """
        while True:
            try:
                user_input = input(prompt).strip()
                
                if not user_input:
                    print("Please enter a number.")
                    continue
                
                try:
                    value = int(user_input)
                except ValueError:
                    print("Please enter a valid integer.")
                    continue
                
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}.")
                    continue
                
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}.")
                    continue
                
                self.input_history.append(user_input)
                return value
                
            except KeyboardInterrupt:
                print("\nInput cancelled.")
                raise
            except EOFError:
                print("\nEnd of input reached.")
                sys.exit(0)
    
    def get_float_input(self, prompt: str, min_value: Optional[float] = None, 
                       max_value: Optional[float] = None) -> float:
        """
        Get validated float input from user.
        
        Args:
            prompt: The input prompt to display
            min_value: Minimum allowed value
            max_value: Maximum allowed value
            
        Returns:
            Validated float input
        """
        while True:
            try:
                user_input = input(prompt).strip()
                
                if not user_input:
                    print("Please enter a number.")
                    continue
                
                try:
                    value = float(user_input)
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}.")
                    continue
                
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}.")
                    continue
                
                self.input_history.append(user_input)
                return value
                
            except KeyboardInterrupt:
                print("\nInput cancelled.")
                raise
            except EOFError:
                print("\nEnd of input reached.")
                sys.exit(0)
    
    def get_menu_choice(self, prompt: str, min_choice: int, max_choice: int) -> int:
        """
        Get a menu choice within specified range.
        
        Args:
            prompt: The input prompt to display
            min_choice: Minimum valid choice
            max_choice: Maximum valid choice
            
        Returns:
            Validated menu choice
        """
        return self.get_integer_input(prompt, min_choice, max_choice)
    
    def get_yes_no_input(self, prompt: str, default: Optional[bool] = None) -> bool:
        """
        Get yes/no input from user.
        
        Args:
            prompt: The input prompt to display
            default: Default value if user just presses Enter
            
        Returns:
            True for yes, False for no
        """
        if default is True:
            prompt += " [Y/n]: "
        elif default is False:
            prompt += " [y/N]: "
        else:
            prompt += " [y/n]: "
        
        while True:
            try:
                user_input = input(prompt).strip().lower()
                
                if not user_input and default is not None:
                    return default
                
                if user_input in ['y', 'yes', 'true', '1']:
                    self.input_history.append(user_input)
                    return True
                elif user_input in ['n', 'no', 'false', '0']:
                    self.input_history.append(user_input)
                    return False
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
                
            except KeyboardInterrupt:
                print("\nInput cancelled.")
                raise
            except EOFError:
                print("\nEnd of input reached.")
                sys.exit(0)
    
    def get_choice_from_list(self, prompt: str, choices: List[Any], 
                            display_func: Optional[callable] = None) -> Any:
        """
        Get user choice from a list of options.
        
        Args:
            prompt: The input prompt to display
            choices: List of available choices
            display_func: Function to display each choice (default: str)
            
        Returns:
            Selected choice from the list
        """
        if not choices:
            raise ValueError("Choice list cannot be empty")
        
        if display_func is None:
            display_func = str
        
        print("\nAvailable options:")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {display_func(choice)}")
        
        choice_index = self.get_menu_choice(prompt, 1, len(choices)) - 1
        return choices[choice_index]
    
    def wait_for_enter(self, message: str = "Press Enter to continue..."):
        """Wait for user to press Enter."""
        try:
            input(message)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            raise
        except EOFError:
            print("\nEnd of input reached.")
            sys.exit(0)
    
    def confirm_action(self, message: str, default: bool = False) -> bool:
        """
        Ask user to confirm an action.
        
        Args:
            message: Confirmation message
            default: Default choice if user just presses Enter
            
        Returns:
            True if confirmed, False otherwise
        """
        return self.get_yes_no_input(f"{message}", default)
    
    def get_input_history(self) -> List[str]:
        """Get the input history."""
        return self.input_history.copy()
    
    def clear_input_history(self):
        """Clear the input history."""
        self.input_history.clear()
