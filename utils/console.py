"""
Console utilities for formatted output and display management.
Provides methods for clean console output with colors and formatting.
"""

import os
import sys
from typing import Optional


class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


class Console:
    """
    Utility class for console operations and formatted output.
    """
    
    @staticmethod
    def clear():
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_colored(text: str, color: str = Colors.RESET, end: str = '\n'):
        """Print text with specified color."""
        print(f"{color}{text}{Colors.RESET}", end=end)
    
    @staticmethod
    def print_header(text: str):
        """Print a formatted header."""
        Console.print_colored(text, Colors.BOLD + Colors.CYAN)
    
    @staticmethod
    def print_success(text: str):
        """Print success message in green."""
        Console.print_colored(f"✓ {text}", Colors.GREEN)
    
    @staticmethod
    def print_error(text: str):
        """Print error message in red."""
        Console.print_colored(f"✗ {text}", Colors.RED)
    
    @staticmethod
    def print_warning(text: str):
        """Print warning message in yellow."""
        Console.print_colored(f"⚠ {text}", Colors.YELLOW)
    
    @staticmethod
    def print_info(text: str):
        """Print info message in blue."""
        Console.print_colored(f"ℹ {text}", Colors.BLUE)
    
    @staticmethod
    def print_welcome():
        """Print welcome message."""
        Console.clear()
        welcome_text = """
    ╔══════════════════════════════════════╗
    ║          AUTO BATTLER GAME           ║
    ║        Console Edition v0.1.0        ║
    ╚══════════════════════════════════════╝
        """
        Console.print_colored(welcome_text, Colors.BOLD + Colors.MAGENTA)
        print("Welcome to the Auto Battler! Build your team and fight!")
        print()
    
    @staticmethod
    def print_separator(char: str = "=", length: int = 50):
        """Print a separator line."""
        print(char * length)
    
    @staticmethod
    def print_boxed(text: str, width: Optional[int] = None):
        """Print text in a box."""
        lines = text.split('\n')
        if width is None:
            width = max(len(line) for line in lines) + 4
        
        print("┌" + "─" * (width - 2) + "┐")
        for line in lines:
            padding = width - len(line) - 4
            print(f"│ {line}{' ' * padding} │")
        print("└" + "─" * (width - 2) + "┘")
    
    @staticmethod
    def print_progress_bar(current: int, total: int, width: int = 30, 
                          label: str = "Progress"):
        """Print a progress bar."""
        if total <= 0:
            percentage = 0
        else:
            percentage = min(current / total, 1.0)
        
        filled = int(width * percentage)
        bar = "█" * filled + "░" * (width - filled)
        
        Console.print_colored(
            f"{label}: [{bar}] {current}/{total} ({percentage*100:.1f}%)",
            Colors.CYAN
        )
    
    @staticmethod
    def get_terminal_size() -> tuple:
        """Get terminal size (width, height)."""
        try:
            size = os.get_terminal_size()
            return size.columns, size.lines
        except OSError:
            return 80, 24  # Default size
    
    @staticmethod
    def center_text(text: str, width: Optional[int] = None) -> str:
        """Center text within specified width."""
        if width is None:
            width, _ = Console.get_terminal_size()
        
        lines = text.split('\n')
        centered_lines = []
        
        for line in lines:
            padding = max(0, (width - len(line)) // 2)
            centered_lines.append(' ' * padding + line)
        
        return '\n'.join(centered_lines)
