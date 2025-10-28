"""
COMP 163 - Project 1: Character Creator & Chronicles
Date: 10/27/2025

AI Usage: ChatGPT assisted with function structure, stat formulas, file I/O, level-up logic, gold system, 
error handling, comments, and example main block for testing throughout all of the code.
"""

import os

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    
    Parameters:
    - name: string, character name
    - character_class: string, must be one of ["Warrior", "Mage", "Rogue", "Cleric"]
    
    Returns:
    - dictionary with keys: name, class, level, strength, magic, health, gold
    - None if invalid class
    
    Notes:
    - Uses calculate_stats() for stat calculation
    - Validates class input
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    
    if character_class not in valid_classes:
        print("Error: Invalid class name.")
        return None

    level = 1  # All new characters start at level 1
    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100  # Starting gold
    }
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == "Warrior":
        strength = 10 + level * 4
        magic = 2 + level * 1
        health = 25 + level * 5
    elif character_class == "Rogue":
        strength = 7 + level * 3
        magic = 4 + level * 2
        health = 20 + level * 4
    elif character_class == "Mage":
        strength = 3 + level * 1
        magic = 12 + level * 4
        health = 18 + level * 3
    elif character_class == "Cleric":
        strength = 5 + level * 2
        magic = 10 + level * 3
        health = 22 + level * 4
    else:
        strength = magic = health = 0

    return strength, magic, health

def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns: True if successful, False if error occurred.
    """
    if character is None or filename == "":
        print("Error: Invalid save attempt.")
        return False

    try:
        with open(filename, "w") as file:
            file.write("Name: " + character["name"] + "\n")
            file.write("Class: " + character["class"] + "\n")
            file.write("Level: " + str(character["level"]) + "\n")
            file.write("Strength: " + str(character["strength"]) + "\n")
            file.write("Magic: " + str(character["magic"]) + "\n")
            file.write("Health: " + str(character["health"]) + "\n")
            file.write("Gold: " + str(character["gold"]) + "\n")
        return True
    except FileNotFoundError:
        print("Error: Directory not found.")
        return False
        
def load_character(filename):
    """
    Loads character from text file.
    Returns: character dictionary if successful, None if file not found or invalid.
    """
    if not os.path.exists(filename):
        print("Error: File not found.")
        return None

    character = {}
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            key = parts[0].lower()
            value = parts[1]
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            character[key] = value

    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            print(f"Error: Missing key '{key}' in character file.")
            return None

    return character

def display_character(character):
    """
    Prints formatted character sheet.
    Returns: None (prints to console).
    """
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("======================\n")

def level_up(character):
    """
    Increases character level and recalculates stats.
    Modifies the character dictionary directly.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += character["level"] * 10  # Increment gold

def random_treasure(character):
    """
    Adds a random gold bonus between 10 and 100.
    """
    import random
    bonus = random.randint(10, 100)
    character["gold"] += bonus
    print(character["name"], "found a treasure chest with", bonus, "gold!")
    
# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    char = create_character("TestHero", "Warrior")
    if char:
        display_character(char)
        save_character(char, "my_character.txt")
        loaded = load_character("my_character.txt")
        if loaded:
            display_character(loaded)
        level_up(char)
        display_character(char)
