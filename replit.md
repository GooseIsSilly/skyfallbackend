# MeteorBackend

## Overview

MeteorBackend is a FastAPI-based game server that provides user management and progression systems for what appears to be a Fortnite-like battle royale game. The system manages player accounts, battle passes, challenges, item shops, cosmetic lockers, and player statistics. It implements a complete progression system with XP, levels, battle pass tiers, challenges, and in-game currency (V-Bucks and Battle Stars).

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Framework
- **FastAPI**: RESTful API server handling all game backend operations
- **File-based Storage**: JSON files for all data persistence instead of a traditional database
- **Token-based Authentication**: Custom token system for user session management

### Authentication System
- **Password Hashing**: Uses bcrypt for secure password storage
- **Token Management**: In-memory token dictionary mapping usernames to authentication tokens
- **Account Creation**: Supports new user registration with hashed passwords

### Data Storage Architecture
- **JSON File System**: All game data stored as JSON files in organized directories
  - `/Accounts/`: Individual player account files
  - `/BattlePass/`: Battle pass reward structures
  - `/ChallengesSets/`: Different challenge configurations
  - `/Shop/`: Item shop configurations
- **Template System**: Uses default account templates for new user creation

### Game Progression System
- **Level System**: XP-based progression with formula y = 200*y for level requirements
- **Battle Pass**: Free and premium tier reward systems with cosmetic unlocks
- **Challenge System**: Multi-tier challenge sets with various objectives and rewards
- **Reward Types**: Supports multiple reward categories (XP, V-Bucks, Battle Stars, cosmetics)

### Cosmetic Management
- **Locker System**: Comprehensive cosmetic inventory management
  - Skins, Backpacks, Gliders, Pickaxes, Contrails, Loading Screens, Emotes
  - Loadout configuration for equipped items
- **Item Categories**: Structured cosmetic item system with unique identifiers

### Challenge and Progression Tracking
- **Challenge Sets**: Modular challenge system supporting different difficulty tiers
- **Progress Tracking**: Individual challenge progress stored per user
- **Reward Distribution**: Automated reward claiming system

## External Dependencies

### Core Dependencies
- **FastAPI**: Web framework for API endpoints
- **uvicorn**: ASGI server for running the FastAPI application
- **bcrypt**: Cryptographic library for password hashing
- **pydantic**: Data validation and settings management

### Development Dependencies
- **Python Standard Library**: Uses json, os, random, string, time, subprocess, asyncio for core functionality
- **sched**: Task scheduling capabilities (imported but usage not visible in provided code)

### File System Dependencies
- Relies on local file system for all data persistence
- No external database connections required
- JSON file structure for all game data storage