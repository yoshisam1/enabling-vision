from enum import Enum

class Game:

    class Turn(Enum):
        NARRATOR = "narrator"
        PLAYER_1 = "player 1"
        PLAYER_2 = "player 2"

    # Have a game state variable (update after every event?)
    game_state = {
        "Round": 0,
        "Turn": Turn.NARRATOR,
        "player 1": { # Replace this with the actual player object
            "name": "Player 1",
            "position": (0, 0),
            "velocity": (0, 0),
            "rotation": 0,
            "scale": 1,
        },
        "player 2": { # Replace this with the actual player object  
            "name": "Player 2",
            "position": (0, 0),
            "velocity": (0, 0),
            "rotation": 0,
            "scale": 1,
        },
    }

    def __init__(self):
        pass

    def commnad_hardware(self, command):
        # tells the hardware to do something

        # Get the current state of the hardware
        state = self.game_state

        # Send the command to the hardware
        self.hardware.send_command(command)

        pass

    def handle_events(self):
        pass

    def update(self):
        # Update game logic here
        pass

    def draw(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.run()
