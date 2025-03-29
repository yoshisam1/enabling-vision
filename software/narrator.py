from typing import Optional

class Narrator:
    def __init__(self):
        self.sound_enabled = False  # For future sound implementation
    
    def announce_move(self, user_name: str, move_name: str, roll: int,
                     damage: int, formula: Optional[str] = None, effects: Optional[str] = None) -> str:
        """Narrate a move being used"""
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
        return "(Super Effective!)"
    
    def announce_turn(self, player_name: str) -> str:
        """Narrate the start of a turn"""
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
        return "\nChoose a move (enter the number): "
    
    def invalid_number(self) -> str:
        """Narrate invalid number input"""
        return "Please enter a number." 