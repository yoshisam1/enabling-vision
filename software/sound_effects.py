from typing import Dict, Optional
import os

class SoundEffects:
    """
    Manages sound effects for the game.
    Provides easy access to sound effect file paths and categories.
    """
    
    # Base directories for sound effects
    SOUNDS_DIR = "public"
    VOICE_ACTORS_DIR = os.path.join(SOUNDS_DIR, "Voice Actors")
    
    # Sound effect categories
    class Category:
        MOVES = "moves"
        UI = "ui"
        AMBIENT = "ambient"
        VOICE = "voice"
        EFFECTS = "effects"
        NUMBERS = "numbers"
    
    # Sound effect file paths organized by category
    SOUNDS: Dict[str, Dict[str, str]] = {
        Category.MOVES: {
            "fire": os.path.join(SOUNDS_DIR, "fire_attack_sound_effect.wav"),
            "water": os.path.join(SOUNDS_DIR, "water_attack_sound_effect.wav"),
            "earth": os.path.join(SOUNDS_DIR, "earth_attack_sound_effect.wav"),
            "normal": os.path.join(SOUNDS_DIR, "normal_hit.wav"),
            "super_effective": os.path.join(SOUNDS_DIR, "super_effective_hit.wav"),
            "stat_up": os.path.join(SOUNDS_DIR, "stat_up_sound_effect.wav"),
            "stat_down": os.path.join(SOUNDS_DIR, "stat_down_sound_effect.wav"),
        },
        Category.UI: {
            "select": os.path.join(SOUNDS_DIR, "select_sound_effect.wav"),
        },
        Category.AMBIENT: {
            "music": os.path.join(SOUNDS_DIR, "music.wav"),
        },
        Category.VOICE: {
            "choose_character": os.path.join(VOICE_ACTORS_DIR, "Voice #1 Choose your Character Class.mp3"),
            "knight_info": os.path.join(VOICE_ACTORS_DIR, "Voice #2 Knight Info.mp3"),
            "wizard_info": os.path.join(VOICE_ACTORS_DIR, "Voice #3 Wizard Info.mp3"),
            "archer_info": os.path.join(VOICE_ACTORS_DIR, "Voice #4 Archer Info.mp3"),
            "choose_move": os.path.join(VOICE_ACTORS_DIR, "Voice #5 Time to choose your move.mp3"),
            "play_again": os.path.join(VOICE_ACTORS_DIR, "Voice #6 Would you like to play again.mp3"),
            "player1": os.path.join(VOICE_ACTORS_DIR, "Player 1.mp3"),
            "player2": os.path.join(VOICE_ACTORS_DIR, "Player 2.mp3"),
            "deals": os.path.join(VOICE_ACTORS_DIR, "deals.mp3"),
            "damage": os.path.join(VOICE_ACTORS_DIR, "Damage.mp3"),
            "rolled_a": os.path.join(VOICE_ACTORS_DIR, "Rolled a.mp3"),
            "player1_win": os.path.join(VOICE_ACTORS_DIR, "Player 1 Wins.mp3"),
            "player2_win": os.path.join(VOICE_ACTORS_DIR, "Player 2 Wins.mp3"),
            # Knight moves
            "boulder_smash": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Knight", "Boulder Smash.mp3"),
            "inferno_counter": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Knight", "Inferno Counter.mp3"),
            "lava_strike": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Knight", "Lava Strike.mp3"),
            "earthen_tremor": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Knight", "Earthen Tremor.mp3"),
            "magma_punch": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Knight", "Magma Punch.mp3"),
            "rock_breaker": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Knight", "Rock Breaker.mp3"),
            # Wizard moves
            "flame_surge": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Wizard", "Flame Surge.mp3"),
            "hydro_blast": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Wizard", "Hydro Blast.mp3"),
            "ember_wave": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Wizard", "Ember Wave.mp3"),
            "steam_burst": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Wizard", "Steam Burst.mp3"),
            "volcanic_surge": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Wizard", "Volcanic Surge.mp3"),
            "tidal_crash": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Wizard", "Tidal Crash.mp3"),
            # Archer moves
            "flame_arrow": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Archer", "Flame Arrow.mp3"),
            "piercing_shot": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Archer", "Piercing Shot.mp3"),
            "searing_volley": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Archer", "Searing Volley.mp3"),
            "rock_barrage": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Archer", "Rock Barrage.mp3"),
            "explosive_shot": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Archer", "Explosive Shot.mp3"),
            "sharpened_quake": os.path.join(VOICE_ACTORS_DIR, "Movesets", "Archer", "Sharpened Quake.mp3"),
        },
        Category.EFFECTS: {
            "player1_increased_attack": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 1 Increased Attack.mp3"),
            "player1_decreased_attack": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 1 Decreased Attack.mp3"),
            "player1_increased_defense": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 1 Increased Defense.mp3"),
            "player1_decreased_defense": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 1 Decreased Defense.mp3"),
            "player2_increased_attack": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 2 Increased Attack.mp3"),
            "player2_decreased_attack": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 2 Decreased Attack.mp3"),
            "player2_increased_defense": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 2 Increased Defense.mp3"),
            "player2_decreased_defense": os.path.join(VOICE_ACTORS_DIR, "Effects", "Player 2 Decreased Defense.mp3"),
            "super_effective": os.path.join(VOICE_ACTORS_DIR, "Effects", "Super Effective.mp3"),
            "not_enough_energy": os.path.join(VOICE_ACTORS_DIR, "Effects", "Not Enough Energy.mp3"),
        },
        Category.NUMBERS: {
            "1": os.path.join(VOICE_ACTORS_DIR, "Numbers", "1.mp3"),
            "2": os.path.join(VOICE_ACTORS_DIR, "Numbers", "2.mp3"),
            "3": os.path.join(VOICE_ACTORS_DIR, "Numbers", "3.mp3"),
            "4": os.path.join(VOICE_ACTORS_DIR, "Numbers", "4.mp3"),
            "5": os.path.join(VOICE_ACTORS_DIR, "Numbers", "5.mp3"),
            "6": os.path.join(VOICE_ACTORS_DIR, "Numbers", "6.mp3"),
            "7": os.path.join(VOICE_ACTORS_DIR, "Numbers", "7.mp3"),
            "8": os.path.join(VOICE_ACTORS_DIR, "Numbers", "8.mp3"),
            "9": os.path.join(VOICE_ACTORS_DIR, "Numbers", "9.mp3"),
            "10": os.path.join(VOICE_ACTORS_DIR, "Numbers", "10.mp3"),
            "11": os.path.join(VOICE_ACTORS_DIR, "Numbers", "11.mp3"),
            "12": os.path.join(VOICE_ACTORS_DIR, "Numbers", "12.mp3"),
            "13": os.path.join(VOICE_ACTORS_DIR, "Numbers", "13.mp3"),
            "14": os.path.join(VOICE_ACTORS_DIR, "Numbers", "14.mp3"),
            "15": os.path.join(VOICE_ACTORS_DIR, "Numbers", "15.mp3"),
            "16": os.path.join(VOICE_ACTORS_DIR, "Numbers", "16.mp3"),
            "17": os.path.join(VOICE_ACTORS_DIR, "Numbers", "17.mp3"),
            "18": os.path.join(VOICE_ACTORS_DIR, "Numbers", "18.mp3"),
            "19": os.path.join(VOICE_ACTORS_DIR, "Numbers", "19.mp3"),
            "20": os.path.join(VOICE_ACTORS_DIR, "Numbers", "20.mp3"),
            "21": os.path.join(VOICE_ACTORS_DIR, "Numbers", "21.mp3"),
            "22": os.path.join(VOICE_ACTORS_DIR, "Numbers", "22.mp3"),
            "23": os.path.join(VOICE_ACTORS_DIR, "Numbers", "23.mp3"),
            "24": os.path.join(VOICE_ACTORS_DIR, "Numbers", "24.mp3"),
            "25": os.path.join(VOICE_ACTORS_DIR, "Numbers", "25.mp3"),
            "26": os.path.join(VOICE_ACTORS_DIR, "Numbers", "26.mp3"),
            "27": os.path.join(VOICE_ACTORS_DIR, "Numbers", "27.mp3"),
            "28": os.path.join(VOICE_ACTORS_DIR, "Numbers", "28.mp3"),
            "29": os.path.join(VOICE_ACTORS_DIR, "Numbers", "29.mp3"),
            "30": os.path.join(VOICE_ACTORS_DIR, "Numbers", "30.mp3"),
            "31": os.path.join(VOICE_ACTORS_DIR, "Numbers", "31.mp3"),
            "32": os.path.join(VOICE_ACTORS_DIR, "Numbers", "32.mp3"),
            "33": os.path.join(VOICE_ACTORS_DIR, "Numbers", "33.mp3"),
            "34": os.path.join(VOICE_ACTORS_DIR, "Numbers", "34.mp3"),
            "35": os.path.join(VOICE_ACTORS_DIR, "Numbers", "35.mp3"),
            "36": os.path.join(VOICE_ACTORS_DIR, "Numbers", "36.mp3"),
            "37": os.path.join(VOICE_ACTORS_DIR, "Numbers", "37.mp3"),
            "38": os.path.join(VOICE_ACTORS_DIR, "Numbers", "38.mp3"),
            "39": os.path.join(VOICE_ACTORS_DIR, "Numbers", "39.mp3"),
            "40": os.path.join(VOICE_ACTORS_DIR, "Numbers", "40.mp3"),
            "41": os.path.join(VOICE_ACTORS_DIR, "Numbers", "41.mp3"),
            "42": os.path.join(VOICE_ACTORS_DIR, "Numbers", "42.mp3"),
            "43": os.path.join(VOICE_ACTORS_DIR, "Numbers", "43.mp3"),
            "44": os.path.join(VOICE_ACTORS_DIR, "Numbers", "44.mp3"),
            "45": os.path.join(VOICE_ACTORS_DIR, "Numbers", "45.mp3"),
            "46": os.path.join(VOICE_ACTORS_DIR, "Numbers", "46.mp3"),
            "47": os.path.join(VOICE_ACTORS_DIR, "Numbers", "47.mp3"),
            "48": os.path.join(VOICE_ACTORS_DIR, "Numbers", "48.mp3"),
            "49": os.path.join(VOICE_ACTORS_DIR, "Numbers", "49.mp3"),
            "50": os.path.join(VOICE_ACTORS_DIR, "Numbers", "50.mp3"),
            "51": os.path.join(VOICE_ACTORS_DIR, "Numbers", "51.mp3"),
            "52": os.path.join(VOICE_ACTORS_DIR, "Numbers", "52.mp3"),
            "53": os.path.join(VOICE_ACTORS_DIR, "Numbers", "53.mp3"),
            "54": os.path.join(VOICE_ACTORS_DIR, "Numbers", "54.mp3"),
            "55": os.path.join(VOICE_ACTORS_DIR, "Numbers", "55.mp3"),
            "56": os.path.join(VOICE_ACTORS_DIR, "Numbers", "56.mp3"),
            "57": os.path.join(VOICE_ACTORS_DIR, "Numbers", "57.mp3"),
            "58": os.path.join(VOICE_ACTORS_DIR, "Numbers", "58.mp3"),
            "59": os.path.join(VOICE_ACTORS_DIR, "Numbers", "59.mp3"),
            "60": os.path.join(VOICE_ACTORS_DIR, "Numbers", "60.mp3"),
            "61": os.path.join(VOICE_ACTORS_DIR, "Numbers", "61.mp3"),
            "62": os.path.join(VOICE_ACTORS_DIR, "Numbers", "62.mp3"),
            "63": os.path.join(VOICE_ACTORS_DIR, "Numbers", "63.mp3"),
            "64": os.path.join(VOICE_ACTORS_DIR, "Numbers", "64.mp3"),
            "65": os.path.join(VOICE_ACTORS_DIR, "Numbers", "65.mp3"),
            "66": os.path.join(VOICE_ACTORS_DIR, "Numbers", "66.mp3"),
            "67": os.path.join(VOICE_ACTORS_DIR, "Numbers", "67.mp3"),
            "68": os.path.join(VOICE_ACTORS_DIR, "Numbers", "68.mp3"),
            "69": os.path.join(VOICE_ACTORS_DIR, "Numbers", "69.mp3"),
            "70": os.path.join(VOICE_ACTORS_DIR, "Numbers", "70.mp3"),
            "71": os.path.join(VOICE_ACTORS_DIR, "Numbers", "71.mp3"),
            "72": os.path.join(VOICE_ACTORS_DIR, "Numbers", "72.mp3"),
            "73": os.path.join(VOICE_ACTORS_DIR, "Numbers", "73.mp3"),
            "74": os.path.join(VOICE_ACTORS_DIR, "Numbers", "74.mp3"),
            "75": os.path.join(VOICE_ACTORS_DIR, "Numbers", "75.mp3"),
            "76": os.path.join(VOICE_ACTORS_DIR, "Numbers", "76.mp3"),
            "77": os.path.join(VOICE_ACTORS_DIR, "Numbers", "77.mp3"),
            "78": os.path.join(VOICE_ACTORS_DIR, "Numbers", "78.mp3"),
            "79": os.path.join(VOICE_ACTORS_DIR, "Numbers", "79.mp3"),
            "80": os.path.join(VOICE_ACTORS_DIR, "Numbers", "80.mp3"),
            "81": os.path.join(VOICE_ACTORS_DIR, "Numbers", "81.mp3"),
            "82": os.path.join(VOICE_ACTORS_DIR, "Numbers", "82.mp3"),
            "83": os.path.join(VOICE_ACTORS_DIR, "Numbers", "83.mp3"),
            "84": os.path.join(VOICE_ACTORS_DIR, "Numbers", "84.mp3"),
            "85": os.path.join(VOICE_ACTORS_DIR, "Numbers", "85.mp3"),
            "86": os.path.join(VOICE_ACTORS_DIR, "Numbers", "86.mp3"),
            "87": os.path.join(VOICE_ACTORS_DIR, "Numbers", "87.mp3"),
            "88": os.path.join(VOICE_ACTORS_DIR, "Numbers", "88.mp3"),
            "89": os.path.join(VOICE_ACTORS_DIR, "Numbers", "89.mp3"),
            "90": os.path.join(VOICE_ACTORS_DIR, "Numbers", "90.mp3"),
            "91": os.path.join(VOICE_ACTORS_DIR, "Numbers", "91.mp3"),
            "92": os.path.join(VOICE_ACTORS_DIR, "Numbers", "92.mp3"),
            "93": os.path.join(VOICE_ACTORS_DIR, "Numbers", "93.mp3"),
            "94": os.path.join(VOICE_ACTORS_DIR, "Numbers", "94.mp3"),
            "95": os.path.join(VOICE_ACTORS_DIR, "Numbers", "95.mp3"),
            "96": os.path.join(VOICE_ACTORS_DIR, "Numbers", "96.mp3"),
            "97": os.path.join(VOICE_ACTORS_DIR, "Numbers", "97.mp3"),
            "98": os.path.join(VOICE_ACTORS_DIR, "Numbers", "98.mp3"),
            "99": os.path.join(VOICE_ACTORS_DIR, "Numbers", "99.mp3"),
            "100": os.path.join(VOICE_ACTORS_DIR, "Numbers", "100.mp3"),
        }
    }
    
    @classmethod
    def get_sound_path(cls, category: str, sound_name: str) -> Optional[str]:
        """
        Get the file path for a specific sound effect
        
        Args:
            category: The category of the sound (e.g., 'moves', 'voice')
            sound_name: The name of the sound effect
            
        Returns:
            The full path to the sound file, or None if not found
        """
        if category in cls.SOUNDS and sound_name in cls.SOUNDS[category]:
            return cls.SOUNDS[category][sound_name]
        return None
    
    @classmethod
    def get_category_sounds(cls, category: str) -> Dict[str, str]:
        """
        Get all sound effects in a category
        
        Args:
            category: The category to get sounds for
            
        Returns:
            Dictionary of sound names to file paths
        """
        return cls.SOUNDS.get(category, {})
    
    @classmethod
    def get_move_sound(cls, move_name: str) -> Optional[str]:
        """
        Get the sound effect for a specific move
        
        Args:
            move_name: The name of the move
            
        Returns:
            The full path to the sound file, or None if not found
        """
        # Convert move name to lowercase and replace spaces with underscores
        sound_name = move_name.lower().replace(" ", "_")
        
        # Map move types to sound effects
        move_type_to_sound = {
            "fire": "fire",
            "water": "water",
            "earth": "earth",
            "normal": "normal",
            "super_effective_hit": "super_effective"
        }
        
        # Try to get the specific sound for the move type
        if sound_name in move_type_to_sound:
            return cls.get_sound_path(cls.Category.MOVES, move_type_to_sound[sound_name])
        
        # Default to normal hit sound
        return cls.get_sound_path(cls.Category.MOVES, "normal")
    
    @classmethod
    def get_ui_sound(cls, action: str) -> Optional[str]:
        """
        Get a UI sound effect
        
        Args:
            action: The UI action (select, etc.)
            
        Returns:
            The full path to the sound file, or None if not found
        """
        return cls.get_sound_path(cls.Category.UI, action)
    
    @classmethod
    def get_victory_sound(cls, player_id: int) -> Optional[str]:
        """
        Get the victory sound for a player
        
        Args:
            player_id: The ID of the winning player (1 or 2)
            
        Returns:
            The full path to the sound file, or None if not found
        """
        sound_name = f"player{player_id}_win"
        return cls.get_sound_path(cls.Category.VOICE, sound_name)
    
    @classmethod
    def get_stat_change_sound(cls, player_id: int, stat: str, is_increase: bool) -> Optional[str]:
        """
        Get the sound effect for a stat change
        
        Args:
            player_id: The ID of the player (1 or 2)
            stat: The stat being changed (attack or defense)
            is_increase: True for stat increase, False for stat decrease
            
        Returns:
            The full path to the sound file
        """
        sound_name = f"player{player_id}_{'increased' if is_increase else 'decreased'}_{stat}"
        return cls.get_sound_path(cls.Category.EFFECTS, sound_name)
    
    @classmethod
    def get_super_effective_sound(cls) -> Optional[str]:
        """
        Get the sound effect for a super effective hit
        
        Returns:
            The full path to the sound file
        """
        return cls.get_sound_path(cls.Category.EFFECTS, "super_effective")
    
    @classmethod
    def get_background_music(cls) -> Optional[str]:
        """
        Get the background music file
        
        Returns:
            The full path to the music file
        """
        return cls.get_sound_path(cls.Category.AMBIENT, "music")
    
    @classmethod
    def get_voice_line(cls, line_name: str) -> Optional[str]:
        """
        Get a voice line
        
        Args:
            line_name: The name of the voice line
            
        Returns:
            The full path to the voice line file
        """
        return cls.get_sound_path(cls.Category.VOICE, line_name)
    
    @classmethod
    def get_number_sound(cls, number: int) -> Optional[str]:
        """
        Get the sound file for a number
        
        Args:
            number: The number to get the sound for (1-100)
            
        Returns:
            The full path to the number sound file, or None if not found
        """
        return cls.get_sound_path(cls.Category.NUMBERS, str(number)) 