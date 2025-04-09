#!/usr/bin/env python3
"""
Test script for playing sound effects without Arduino.
This script allows testing all sound effects in the game.
"""

import os
import time
from playsound import playsound
from software.sound_effects import SoundEffects

def test_sound(category: str, sound_name: str, description: str):
    """Test a single sound effect"""
    print(f"\nTesting {description}...")
    sound_path = SoundEffects.get_sound_path(category, sound_name)
    if sound_path and os.path.exists(sound_path):
        print(f"Playing: {sound_path}")
        try:
            playsound(sound_path)
        except Exception as e:
            print(f"Error playing sound: {e}")
    else:
        print(f"Sound file not found: {sound_path}")

def main():
    """Test all sound effects"""
    print("Starting sound effects test...")
    
    # Test move sounds
    print("\n=== Testing Move Sounds ===")
    test_sound(SoundEffects.Category.MOVES, "fire", "Fire attack")
    test_sound(SoundEffects.Category.MOVES, "water", "Water attack")
    test_sound(SoundEffects.Category.MOVES, "earth", "Earth attack")
    test_sound(SoundEffects.Category.MOVES, "normal", "Normal hit")
    test_sound(SoundEffects.Category.MOVES, "super_effective", "Super effective hit")
    test_sound(SoundEffects.Category.MOVES, "stat_up", "Stat up")
    test_sound(SoundEffects.Category.MOVES, "stat_down", "Stat down")
    
    # Test UI sounds
    print("\n=== Testing UI Sounds ===")
    test_sound(SoundEffects.Category.UI, "select", "Select sound")
    
    # Test ambient sounds
    print("\n=== Testing Ambient Sounds ===")
    test_sound(SoundEffects.Category.AMBIENT, "music", "Background music")
    
    # Test voice lines
    print("\n=== Testing Voice Lines ===")
    test_sound(SoundEffects.Category.VOICE, "choose_character", "Choose character")
    test_sound(SoundEffects.Category.VOICE, "knight_info", "Knight info")
    test_sound(SoundEffects.Category.VOICE, "wizard_info", "Wizard info")
    test_sound(SoundEffects.Category.VOICE, "archer_info", "Archer info")
    test_sound(SoundEffects.Category.VOICE, "choose_move", "Choose move")
    test_sound(SoundEffects.Category.VOICE, "play_again", "Play again")
    test_sound(SoundEffects.Category.VOICE, "player1", "Player 1")
    test_sound(SoundEffects.Category.VOICE, "player2", "Player 2")
    test_sound(SoundEffects.Category.VOICE, "deals", "Deals")
    test_sound(SoundEffects.Category.VOICE, "damage", "Damage")
    test_sound(SoundEffects.Category.VOICE, "rolled_a", "Rolled a")
    test_sound(SoundEffects.Category.VOICE, "player1_win", "Player 1 wins")
    test_sound(SoundEffects.Category.VOICE, "player2_win", "Player 2 wins")
    
    # Test effect sounds
    print("\n=== Testing Effect Sounds ===")
    test_sound(SoundEffects.Category.EFFECTS, "player1_increased_attack", "Player 1 increased attack")
    test_sound(SoundEffects.Category.EFFECTS, "player1_decreased_attack", "Player 1 decreased attack")
    test_sound(SoundEffects.Category.EFFECTS, "player1_increased_defense", "Player 1 increased defense")
    test_sound(SoundEffects.Category.EFFECTS, "player1_decreased_defense", "Player 1 decreased defense")
    test_sound(SoundEffects.Category.EFFECTS, "player2_increased_attack", "Player 2 increased attack")
    test_sound(SoundEffects.Category.EFFECTS, "player2_decreased_attack", "Player 2 decreased attack")
    test_sound(SoundEffects.Category.EFFECTS, "player2_increased_defense", "Player 2 increased defense")
    test_sound(SoundEffects.Category.EFFECTS, "player2_decreased_defense", "Player 2 decreased defense")
    test_sound(SoundEffects.Category.EFFECTS, "super_effective", "Super effective")
    test_sound(SoundEffects.Category.EFFECTS, "not_enough_energy", "Not enough energy")
    
    # Test number sounds
    print("\n=== Testing Number Sounds ===")
    print("Testing numbers 1-10...")
    for i in range(1, 11):
        test_sound(SoundEffects.Category.NUMBERS, str(i), f"Number {i}")
        time.sleep(0.5)  # Small delay between numbers
    
    print("\nSound effects test completed!")

if __name__ == "__main__":
    main() 