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
            
        # Get input from user
        key = input()
        
        if player_id == 1:
            # For Player 1 (numeric keys)
            if key in "123456":
                button_num = int(key)
                print(f"Player 1 pressed button {button_num}")
                return button_num
        else:
            # For Player 2 (qwerty keys)
            if key in "qwerty":
                # Convert qwerty to 1-6
                button_mapping = {"q": 1, "w": 2, "e": 3, "r": 4, "t": 5, "y": 6}
                button_num = button_mapping[key]
                print(f"Player 2 pressed button {button_num}")
                return button_num
                
        # Invalid key or no key pressed
        print("Invalid input!")
        return None
        