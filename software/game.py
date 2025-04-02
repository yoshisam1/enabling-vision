from enum import Enum
from .character import Character
from .narrator import Narrator
import time  # Add this import at the top of the file

class GameState:
    class Turn(Enum):
        NARRATOR = "narrator"
        PLAYER_1 = "player 1"
        PLAYER_2 = "player 2"

    def __init__(self):
        self.round = 0
        self.turn = self.Turn.NARRATOR
        self.player1 = None  # Will hold Character object
        self.player2 = None  # Will hold Character object
        self.narrator = Narrator()   # For future narrator implementation

class Game:
    def __init__(self, hardware_command_listener):
        print("Welcome to the Battle Game!")
        self.hardware_command_listener = hardware_command_listener
        self.state = GameState()

    def run(self):
        self.setup_players()
        self.battle()
        exit()

    # Need to check other class to ask for input through hardware
    def setup_players(self):
        # Player 1 setup
        print("\nPlayer 1 setup:")
        self.state.player1 = Character("Player 1")
        
        # Use menu navigation for Player 1 character selection
        class_selected = self._navigate_character_select(1)
        self.state.player1.select_character_class(class_selected)
        
        # Player 2 setup
        print("\nPlayer 2 setup:")
        self.state.player2 = Character("Player 2")
        
        # Use menu navigation for Player 2 character selection
        class_selected = self._navigate_character_select(2)
        self.state.player2.select_character_class(class_selected)
    
    def _navigate_character_select(self, player_id):
        """Use single button navigation to select a character class"""
        class_options = [
            "Knight - Moderate health, high defense, low attack",
            "Wizard - High health, low defense, moderate attack",
            "Archer - Low health, moderate defense, high attack"
        ]
        
        current_selection = 0
        selection_made = False
        
        # Display initial options with highlighting
        self._display_menu_options(class_options, current_selection, player_id)
        print("Single press: Move Down, Double press: Select")
        
        while not selection_made:
            # Get navigation input
            button = self.hardware_command_listener.on_command("check_button", player_id=player_id)
            
            if button == "DOWN":
                # Move selection down (wrapping around to top if needed)
                current_selection = (current_selection + 1) % len(class_options)
                self._display_menu_options(class_options, current_selection, player_id)
                print("Single press: Move Down, Double press: Select")
                
            elif button == "SELECT":
                # Confirm selection
                selection_made = True
                print(f"Player {player_id} selected: {class_options[current_selection]}")
            
            # Add delay after any input processing
            if button is not None:
                time.sleep(1)
        
        return current_selection + 1
    
    def _display_menu_options(self, options, selected_index, player_id):
        """Display menu options with the selected one highlighted"""
        print(f"\nPlayer {player_id}, choose your character class:")
        for i, option in enumerate(options):
            if i == selected_index:
                print(f"→ {i+1}. {option} ←")  # Highlight with arrows
            else:
                print(f"  {i+1}. {option}")
    
    # This is where we request the hardware for input and output
    def battle(self):
        print("\nBattle begins!")
        
        while self.state.player1.is_alive and self.state.player2.is_alive:
            if self.state.turn == GameState.Turn.PLAYER_1:
                self.player_turn(self.state.player1, self.state.player2)
                self.state.turn = GameState.Turn.PLAYER_2
                
            elif self.state.turn == GameState.Turn.PLAYER_2:
                self.player_turn(self.state.player2, self.state.player1)
                self.state.turn = GameState.Turn.NARRATOR
                
            elif self.state.turn == GameState.Turn.NARRATOR:
                print("\nNarrator's Turn!")
                self.state.round += 1
                print(f"Round {self.state.round} completed!")
                self.state.turn = GameState.Turn.PLAYER_1
        
        # Battle ended
        winner = self.state.player1 if self.state.player1.is_alive else self.state.player2
        self.play_victory_sound()

    def player_turn(self, player, opponent):
        print(self.state.narrator.announce_turn(player.name))
        print(player)
        
        # Show available moves
        available_moves = player.get_available_moves()
        if not available_moves:
            print(self.state.narrator.announce_no_moves())
            return
        
        # Determine which player is active
        player_id = 1 if player == self.state.player1 else 2
        
        # Use menu navigation for move selection
        move_options = [f"{move.name} - {move.effect_description}" for move in available_moves]
        selected_index = self._navigate_move_select(move_options, player_id)
        
        # Use the selected move
        move_index = player.moves.index(available_moves[selected_index])
        success, message = player.use_move(move_index, opponent)
        print(message)
    
    def _navigate_move_select(self, options, player_id):
        """Use single button navigation to select a move"""
        current_selection = 0
        selection_made = False
        
        # Display initial options with highlighting
        self._display_menu_options(options, current_selection, player_id)
        print(self.state.narrator.request_move_choice())
        print("Single press: Move Down, Double press: Select")
        
        while not selection_made:
            # Get navigation input
            button = self.hardware_command_listener.on_command("check_button", player_id=player_id)
            
            if button == "DOWN":
                # Move selection down (wrapping around to top if needed)
                current_selection = (current_selection + 1) % len(options)
                self._display_menu_options(options, current_selection, player_id)
                print(self.state.narrator.request_move_choice())
                print("Single press: Move Down, Double press: Select")
                
            elif button == "SELECT":
                # Confirm selection
                selection_made = True
                print(f"Selected: {options[current_selection]}")
            
            # Add delay after any input processing
            if button is not None:
                time.sleep(1)
        
        return current_selection

    def play_victory_sound(self):
        self.hardware_command_listener.on_command("play_audio", file_path="victory.mp3")