from enum import Enum
from .character import Character
from .narrator import Narrator
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
        
        # Use hardware input for Player 1 character selection
        print(self.state.narrator.request_character_selection())
        class_selected = False
        
        while not class_selected:
            # Request button press from Player 1
            button = self.hardware_command_listener.on_command("check_button", player_id=1)
            
            # If a button was pressed and it's valid for character selection (1-3)
            if button is not None and 1 <= button <= 3:
                self.state.player1.select_character_class(button)
                class_selected = True
            elif button is not None:
                # Button press was invalid
                print(self.state.narrator.invalid_choice())
        
        # Player 2 setup
        print("\nPlayer 2 setup:")
        self.state.player2 = Character("Player 2")
        
        # Use hardware input for Player 2 character selection
        print(self.state.narrator.request_character_selection())
        class_selected = False
        
        while not class_selected:
            # Request button press from Player 2
            button = self.hardware_command_listener.on_command("check_button", player_id=2)
            
            # Convert button to number if using qwerty mapping
            # If a button was pressed and it's valid for character selection (1-3)
            if button is not None and 1 <= button <= 3:
                self.state.player2.select_character_class(button)
                class_selected = True
            elif button is not None:
                # Button press was invalid
                print(self.state.narrator.invalid_choice())
    
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
        
        print(self.state.narrator.show_available_moves(available_moves))
        
        # Determine which player is active
        player_id = 1 if player == self.state.player1 else 2
        
        # Get move choice using hardware_command_listener
        print(self.state.narrator.request_move_choice())
        move_selected = False

        # if player_id == 1:
        #     # Player 1 uses numeric keys 1-6
        #     prompt = "Player 1: Press a button (1-6): "
        # else:
        #     # Player 2 uses qwerty
        #     prompt = "Player 2: Press a button (q,w,e,r,t,y): "
        
        while not move_selected:
            # Request button press from the hardware
            button = self.hardware_command_listener.on_command("check_button", player_id=player_id)
            
            # If a button was pressed and it's valid
            if button is not None and 1 <= button <= len(available_moves):
                # Select the corresponding move
                move_index = player.moves.index(available_moves[button-1])
                success, message = player.use_move(move_index, opponent)
                print(message)
                move_selected = True
            elif button is not None:
                # Button press was invalid
                print(self.state.narrator.invalid_choice())

    def play_victory_sound(self):
        self.hardware_command_listener.on_command("play_audio", file_path="victory.mp3")