# Please return in a dictionary format

class Hardware:
    def __init__(self):
        """Initialize hardware interfaces"""
        # Setup audio, motors, buttons, etc.
        pass
    
    def play_audio(self, file_path):
        """Play audio file"""
        print(f"Playing audio: {file_path}")
        # Actual implementation depends on your hardware
    
    def vibrate(self, player_id, pattern):
        """Activate vibration motor"""
        print(f"Player {player_id} controller vibrating with pattern: {pattern}")
        # Actual implementation depends on your hardware
        
    # sample implementation
    def check_button(self, player_id):
        """Check if a button is pressed for the given player"""
        if player_id == 1:
            # Player 1 uses arrow keys and enter
            prompt = "Player 1 controls: ↑(8), ↓(2), SELECT(5): "
            up_key = "8"
            down_key = "2" 
            select_key = "5"
        else:
            # Player 2 uses WASD and space
            prompt = "Player 2 controls: UP(w), DOWN(s), SELECT(e): "
            up_key = "w"
            down_key = "s"
            select_key = "e"
            
        # Get input from user
        key = input(prompt)
        
        if player_id == 1:
            if key == up_key:
                return "UP"
            elif key == down_key:
                return "DOWN"
            elif key == select_key:
                return "SELECT"
        else:
            if key == up_key:
                return "UP"
            elif key == down_key:
                return "DOWN"
            elif key == select_key:
                return "SELECT"
                
        # Invalid key or no key pressed
        print("Invalid input!")
        return None
        