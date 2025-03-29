# This is the main driver that will call the other two drivers of each sub-system
from hardware.hardware import Hardware
from software.game import Game

class HardwareCommandListener:
    def on_command(self, command, **params):
        """Handle commands from the game (implements HardwareCommandListener)"""
        pass

class Bridge(HardwareCommandListener):
    def __init__(self):
        self.hardware = Hardware()
        self.software = Game(self)
    
    # This is where we request the hardware for input and output
    def run(self):
        self.software.run()

    # Is called by the game
    def on_command(self, command, **params):
        """Handle commands from the game (implements HardwareCommandListener)"""
        if command == "play_audio":
            self.hardware.play_audio(params["file_path"])
            return True
        
        elif command == "vibrate":
            self.hardware.vibrate(params["player_id"], params["pattern"])
            return True
        
        elif command == "check_button":
            return self.hardware.check_button(params["player_id"])

        return False

if __name__ == "__main__":
    bridge = Bridge()
    bridge.run()