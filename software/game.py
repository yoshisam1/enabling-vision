from enum import Enum
from character import Character, CharacterClass
from narrator import Narrator

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
    def __init__(self):
        print("Welcome to the Battle Game!")
        self.state = GameState()
        self.run()

    def run(self):
        self.setup_players()
        self.battle()
        exit()

    def setup_players(self):
        # Player 1 setup
        print("\nPlayer 1 setup:")
        self.state.player1 = Character("Player 1")
        self.state.player1.select_character_class()
        
        # Player 2 setup
        print("\nPlayer 2 setup:")
        self.state.player2 = Character("Player 2")
        self.state.player2.select_character_class()
    
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
        print(f"\nBattle ended! {winner.name} is victorious!")

    def player_turn(self, player, opponent):
        print(self.state.narrator.announce_turn(player.name))
        print(player)
        
        # Show available moves
        available_moves = player.get_available_moves()
        if not available_moves:
            print(self.state.narrator.announce_no_moves())
            return
        
        print(self.state.narrator.show_available_moves(available_moves))
        
        # Get move choice
        while True:
            try:
                choice = int(input(self.state.narrator.request_move_choice()))
                if 1 <= choice <= len(available_moves):
                    move_index = player.moves.index(available_moves[choice-1])
                    success, message = player.use_move(move_index, opponent)
                    print(message)
                    return
                else:
                    print(self.state.narrator.invalid_choice())
            except ValueError:
                print(self.state.narrator.invalid_number())

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
        print(f"\nBattle ended! {winner.name} is victorious!")

if __name__ == "__main__":
    game = Game()