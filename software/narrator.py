from typing import Optional
from .sound_effects import SoundEffects

class Narrator:
    def __init__(self, hardware_command_listener=None):
        self.hardware_command_listener = hardware_command_listener
        self.sound_enabled = hardware_command_listener is not None
    
    def play_voice_line(self, line_name: str) -> None:
        """Play a voice line if sound is enabled"""
        if self.sound_enabled:
            # Handle moveset descriptions
            if line_name in ["boulder_smash", "inferno_counter", "lava_strike", "earthen_tremor", "magma_punch", "rock_breaker",
                           "flame_surge", "hydro_blast", "ember_wave", "steam_burst", "volcanic_surge", "tidal_crash",
                           "flame_arrow", "piercing_shot", "searing_volley", "rock_barrage", "explosive_shot", "sharpened_quake"]:
                voice_line = SoundEffects.get_voice_line(line_name)
            else:
                voice_line = SoundEffects.get_voice_line(line_name)
            if voice_line:
                self.hardware_command_listener.on_command("play_audio", file_path=voice_line)
    
    def play_move_sound(self, move_name: str) -> None:
        """Play a move sound effect if sound is enabled"""
        if self.sound_enabled:
            move_sound = SoundEffects.get_move_sound(move_name)
            if move_sound:
                self.hardware_command_listener.on_command("play_audio", file_path=move_sound)
    
    def play_super_effective_sound(self) -> None:
        """Play super effective sound if sound is enabled"""
        if self.sound_enabled:
            sound = SoundEffects.get_super_effective_sound()
            if sound:
                self.hardware_command_listener.on_command("play_audio", file_path=sound)
    
    def play_stat_change_sound(self, player_id: int, stat: str, is_increase: bool) -> None:
        """Play stat change sound if sound is enabled"""
        if self.sound_enabled:
            sound = SoundEffects.get_stat_change_sound(player_id, stat, is_increase)
            if sound:
                self.hardware_command_listener.on_command("play_audio", file_path=sound)
    
    def play_victory_sound(self, player_id: int) -> None:
        """Play victory sound if sound is enabled"""
        if self.sound_enabled:
            sound = SoundEffects.get_victory_sound(player_id)
            if sound:
                self.hardware_command_listener.on_command("play_audio", file_path=sound)
    
    def announce_move(self, user_name: str, move_name: str, roll: int,
                     damage: int, formula: Optional[str] = None, effects: Optional[str] = None) -> str:
        """Narrate a move being used"""
        self.play_move_sound(move_name)
        message = f"{user_name} used {move_name}! (Rolled {roll})"
        if effects:
            message += f" {effects}"
        if formula:
            message += f" Damage calculation: {formula} = {damage}!"
        else:
            message += f" Dealt {damage} damage!"
        return message
    
    def announce_healing(self, user_name: str, heal_amount: int) -> str:
        """Narrate healing"""
        return f"{user_name} healed {heal_amount} HP!"
    
    def announce_stat_change(self, target_name: str, stat: str, amount: int) -> str:
        """Narrate stat changes"""
        direction = "raised" if amount > 0 else "lowered"
        return f"{target_name}'s {stat} {direction} by {abs(amount)}!"
    
    def announce_special_effect(self, effect_description: str) -> str:
        """Narrate special effects"""
        return effect_description
    
    def announce_no_moves(self) -> str:
        """Narrate when no moves are available"""
        return "No moves available!"
    
    def announce_move_depleted(self, move_name: str) -> str:
        """Narrate when a move has no uses left"""
        return f"{move_name} has no uses left!"
    
    def announce_super_effective(self) -> str:
        """Narrate when a move is super effective"""
        self.play_super_effective_sound()
        return "(Super Effective!)"
    
    def announce_turn(self, player_name: str) -> str:
        """Narrate the start of a turn"""
        player_id = 1 if "1" in player_name else 2
        self.play_voice_line(f"player{player_id}")
        return f"\n{player_name}'s turn!"
    
    def show_available_moves(self, moves: list) -> str:
        """Display available moves"""
        output = "\nAvailable moves:"
        for i, move in enumerate(moves):
            output += f"\n{i+1}. {move.name} - {move.effect_description}"
        return output
    
    def invalid_choice(self) -> str:
        """Narrate invalid move choice"""
        return "Invalid choice. Please try again."
    
    def request_move_choice(self) -> str:
        """Ask for move choice"""
        self.play_voice_line("choose_move")
        return "\nChoose a move (Player 1: 1-6, Player 2: q,w,e,r,t,y): "
    
    def invalid_number(self) -> str:
        """Narrate invalid number input"""
        return "Please enter a number."
    
    def request_character_selection(self, player_id: int) -> str:
        """Request character selection and play appropriate voice lines"""
        self.play_voice_line(f"player{player_id}")
        self.play_voice_line("choose_character")
        return """\nChoose your character class:
                    1. Knight - Moderate health, high defense, low attack
                    2. Wizard - High health, low defense, moderate attack
                    3. Archer - Low health, moderate defense, high attack"""
    
    def announce_character_info(self, character_class: str) -> None:
        """Play character class information voice line"""
        self.play_voice_line(f"{character_class.lower()}_info")
    
    def announce_victory(self, winner_name: str) -> None:
        """Announce victory and play victory sound"""
        player_id = 1 if "1" in winner_name else 2
        self.play_victory_sound(player_id)
    
    def play_knight_move_description(self, move_name: str) -> None:
        """Play a Knight move description if sound is enabled"""
        if self.sound_enabled:
            voice_line = SoundEffects.get_voice_line(move_name)
            if voice_line:
                self.hardware_command_listener.on_command("play_audio", file_path=voice_line)
    
    def play_wizard_move_description(self, move_name: str) -> None:
        """Play a Wizard move description if sound is enabled"""
        if self.sound_enabled:
            voice_line = SoundEffects.get_voice_line(move_name)
            if voice_line:
                self.hardware_command_listener.on_command("play_audio", file_path=voice_line)
    
    def play_archer_move_description(self, move_name: str) -> None:
        """Play an Archer move description if sound is enabled"""
        if self.sound_enabled:
            voice_line = SoundEffects.get_voice_line(move_name)
            if voice_line:
                self.hardware_command_listener.on_command("play_audio", file_path=voice_line)
    
    def play_select_sound(self) -> None:
        """Play the select sound effect if sound is enabled"""
        if self.sound_enabled:
            sound = SoundEffects.get_ui_sound("select")
            if sound:
                self.hardware_command_listener.on_command("play_audio", file_path=sound) 