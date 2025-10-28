#[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21233283&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge

## 📚 Project Documentation

### Game Concept  
Players create characters in a fantasy RPG world with four classes: Warrior, Mage, Rogue, and Cleric. Characters have unique stats and starting gold, can level up, view stats, and save/load progress.

### Design Choices  
- Stat formulas designed for clarity and balance:  
  - **Warrior:** High strength and health, low magic  
  - **Mage:** High magic, low strength, medium health  
  - **Rogue:** Medium strength and magic, low health  
  - **Cleric:** High magic and moderate strength/health  
- Stats scale by level for consistent progression.  
- Gold also scales with level to reward player advancement.  
- All calculations are formula-based for predictable testing.  
- Robust error handling ensures invalid inputs and missing files are managed gracefully.  
- The `load_character` function validates that all mandatory fields (e.g., name, class, level) are present in the saved file.

### Bonus Creative Features  
- Gold system scales dynamically with level.  
- Level-up recalculates stats and dynamically increases gold as the character progresses.  
- Bonus function for additional gold tracking and management:  
  - `random_treasure(character)` - Adds a random gold bonus between 10 and 100.  
- Optional story hooks for future narrative expansion.  

### AI Usage  
ChatGPT assisted with the entire code implementation, including function structure, stat formulas, file I/O, level-up logic, gold system, and documentation.  

### How to Run  

1. **Run tests:**
   ```bash
   python -m pytest tests/test_character_creation.py -v

2. **Run main program:**
    ```bash
python project1_starter.py


3. **Follow prompts in the main program to create a character, view stats, save/load progress, and level up.**
