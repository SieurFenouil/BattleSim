# Auto Battler Game

## Overview

A bare-bones console-based auto battler game foundation built in Python. This provides only the essential development environment structure with console utilities and input handling. The user will implement all game mechanics themselves, including unit progression, combat system, battle mechanics, and AI decision-making. Currently contains just a basic main menu and placeholder for game implementation.

## User Preferences

- **Communication style**: Simple, everyday language
- **Development approach**: User handles all file changes and commits; agent provides reviews and guidance only
- **Git workflow**: User maintains full control over commit history

## System Architecture

### Core Game Architecture
- **Modular Design**: Organized into distinct packages (`game/`, `utils/`) with clear separation of concerns
- **Minimal Foundation**: Basic main.py with console interface and placeholder for user implementation
- **Development Ready**: Clean structure for user to add custom game logic and mechanics

### Game Logic Components
- **Placeholder Implementation**: Core game mechanics (units, battles, progression) removed per user request
- **Ready for Custom Implementation**: User will code their own battle system, unit progression, AI mechanics, and combat logic
- **Foundation Only**: Current structure provides base framework for user's custom game development

### User Interface Architecture
- **Console-Based Interface**: Terminal/console application with ANSI color support for enhanced visual feedback
- **Input Validation**: Centralized input handling with validation for different input types (strings, menu choices, numbers)
- **Formatted Output**: Utility classes for consistent formatting, colors, and screen management

### Data Management
- **In-Memory Storage**: All game state maintained in memory during runtime
- **No Persistence**: Currently no save/load functionality (marked as future feature)
- **Object State**: Game data managed through object properties and relationships

### Error Handling
- **Input Validation**: Comprehensive input validation with user-friendly error messages
- **Graceful Degradation**: Try-catch blocks around critical operations with fallback behaviors
- **User Guidance**: Clear prompts and instructions for user interactions

## External Dependencies

### Standard Library Dependencies
- **sys**: System-specific parameters and functions for path management
- **os**: Operating system interface for console operations (clear screen)
- **time**: Time-related functions for battle simulation delays
- **random**: Random number generation for battle mechanics and unit creation
- **typing**: Type hints for better code documentation and IDE support

### No External Libraries
- Pure Python implementation using only standard library modules
- No database connections or external APIs
- No web frameworks or networking components
- Self-contained console application