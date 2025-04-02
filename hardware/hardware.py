# Please return in a dictionary format

from pymata4 import pymata4
from playsound import playsound
import time

class Hardware:
    def __init__(self):
        """Initialize hardware interfaces"""
        try:
            # Setup arduino connection
            self.arduino = pymata4.Pymata4()

            # Pin definitions
            self.button_1_pin = 6
            self.button_2_pin = 7
            self.potentio_1_pin = 0
            self.potentio_2_pin = 1
            self.motor_1_en = 9
            self.motor_2_en = 10
            self.motor_dir_pin1 = 3
            self.motor_dir_pin2 = 4

            # Setup pins
            self.arduino.set_pin_mode_analog_input(self.potentio_1_pin)
            self.arduino.set_pin_mode_analog_input(self.potentio_2_pin)
            self.arduino.set_pin_mode_digital_input(self.button_1_pin)
            self.arduino.set_pin_mode_digital_input(self.button_2_pin)
            
            self.arduino.set_pin_mode_digital_output(self.motor_dir_pin1)
            self.arduino.set_pin_mode_digital_output(self.motor_dir_pin2)
            self.arduino.set_pin_mode_pwm_output(self.motor_1_en)
            self.arduino.set_pin_mode_pwm_output(self.motor_2_en)
            
            self.hardware_enabled = True
            print("Hardware interface initialized successfully")
            
        except Exception as e:
            print(f"Failed to initialize hardware: {e}")
            print("Falling back to keyboard input")
            self.hardware_enabled = False
    
    def play_audio(self, file_path):
        """Play audio file"""
        print(f"Playing audio: {file_path}")
        try:
            playsound(file_path)
        except Exception as e:
            print(f"Error playing audio: {e}")

    def vibration_pattern1(self, player_motor):
        """Vibrate the motor with pattern 1: two pulses"""
        for iter in range(2):
            self.arduino.digital_write(self.motor_dir_pin1, 1)
            self.arduino.digital_write(self.motor_dir_pin2, 0)
            self.arduino.pwm_write(player_motor, 255)
            time.sleep(1)
            self.arduino.digital_write(self.motor_dir_pin1, 0)
            self.arduino.digital_write(self.motor_dir_pin2, 0)
            self.arduino.pwm_write(player_motor, 0)
            time.sleep(0.2)

    def vibration_alter_intensity(self, player_motor):
        """Vibrate with increasing then decreasing intensity"""
        for intensity in range(0, 255, 25):  # Step by 25 to make it faster
            self.arduino.digital_write(self.motor_dir_pin1, 1)
            self.arduino.digital_write(self.motor_dir_pin2, 0)
            self.arduino.pwm_write(player_motor, intensity)
            time.sleep(0.05)  # Shorter sleep for smoother effect

        for intensity in range(255, 0, -25):
            self.arduino.digital_write(self.motor_dir_pin1, 1)
            self.arduino.digital_write(self.motor_dir_pin2, 0)
            self.arduino.pwm_write(player_motor, intensity)
            time.sleep(0.05)

        self.arduino.digital_write(self.motor_dir_pin1, 0)
        self.arduino.digital_write(self.motor_dir_pin2, 0)
        self.arduino.pwm_write(player_motor, 0)

    def vibrate(self, player_id, pattern):
        """Activate vibration motor with specified pattern"""
        print(f"Player {player_id} controller vibrating with pattern: {pattern}")
        
        if not self.hardware_enabled:
            return
            
        # Select the appropriate motor
        if player_id == 1:
            player_motor = self.motor_1_en
        else:
            player_motor = self.motor_2_en

        # Pattern selection
        if pattern == "turn" or pattern == 1:
            self.vibration_pattern1(player_motor)
        elif pattern == "victory" or pattern == 2:
            self.vibration_alter_intensity(player_motor)
        else:
            # Default pattern
            self.arduino.digital_write(self.motor_dir_pin1, 1)
            self.arduino.digital_write(self.motor_dir_pin2, 0)
            self.arduino.pwm_write(player_motor, 200)
            time.sleep(0.5)
            self.arduino.digital_write(self.motor_dir_pin1, 0)
            self.arduino.digital_write(self.motor_dir_pin2, 0)
            self.arduino.pwm_write(player_motor, 0)

    def check_button(self, player_id):
        """Check for player input (DOWN/SELECT) using single button with pattern detection"""
        if not self.hardware_enabled:
            # Fallback to keyboard input if hardware isn't available
            return self._check_button_keyboard(player_id)
            
        # Hardware-based input
        player_button = self.button_1_pin if player_id == 1 else self.button_2_pin
        
        # Constants for double-click detection
        DOUBLE_CLICK_WINDOW = 0.5  # seconds between clicks to count as double
        DEBOUNCE_TIME = 0.05  # seconds to wait for button debounce
        
        # Give user some time to respond, but don't block indefinitely
        start_time = time.time()
        last_press_time = 0
        press_count = 0
        
        while (time.time() - start_time) < 5:  # 5 second timeout
            button_state = self.arduino.digital_read(player_button)[0]
            current_time = time.time()
            
            if button_state == 1:  # Button is pressed
                if current_time - last_press_time > DEBOUNCE_TIME:
                    press_count += 1
                    last_press_time = current_time
                    
                    # Wait a bit to avoid immediate re-triggering
                    time.sleep(DEBOUNCE_TIME)
                    
                    # Wait briefly to see if there's a second press
                    check_time = current_time
                    while current_time - check_time < DOUBLE_CLICK_WINDOW:
                        current_time = time.time()
                        if self.arduino.digital_read(player_button)[0] == 1:
                            if current_time - last_press_time > DEBOUNCE_TIME:
                                # Double click detected
                                print(f"Player {player_id} double-clicked (SELECT)")
                                return "SELECT"
                
                    # If we get here, it was a single press
                    print(f"Player {player_id} single-clicked (DOWN)")
                    return "DOWN"
                
            time.sleep(0.05)  # Small delay to prevent CPU overuse
            
        return None

    def _check_button_keyboard(self, player_id):
        """Fallback keyboard input method for single-button setup"""
        if player_id == 1:
            prompt = "Player 1 controls: Single press(2), Double press(5): "
            down_key = "2"
            select_key = "5"
        else:
            prompt = "Player 2 controls: Single press(s), Double press(e): "
            down_key = "s"
            select_key = "e"
            
        key = input(prompt)
        
        if key == down_key:
            return "DOWN"
        elif key == select_key:
            return "SELECT"
            
        print("Invalid input!")
        return None
        
    def shutdown(self):
        """Safely shutdown the hardware"""
        if self.hardware_enabled:
            try:
                self.arduino.digital_write(self.motor_dir_pin1, 0)
                self.arduino.digital_write(self.motor_dir_pin2, 0)
                self.arduino.pwm_write(self.motor_1_en, 0)
                self.arduino.pwm_write(self.motor_2_en, 0)
                self.arduino.shutdown()
                print("Hardware shutdown complete")
            except Exception as e:
                print(f"Error during hardware shutdown: {e}")
        