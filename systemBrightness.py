# systemBrightness.py
import screen_brightness_control as sbc

class SystemBrightness:
    def __init__(self):
        # You may not need anything special for initialization, this is handled by the library
        pass
    
    def get_brightness(self):
        """
        Reads the current brightness level of the screen.
        """
        try:
            brightness = sbc.get_brightness()
            print(f"Current brightness: {brightness}%")
            return brightness
        except Exception as e:
            print("Error reading brightness:", e)
            return None
    
    def set_brightness(self, brightness_level):
        """
        Sets the brightness level of the screen.
        """
        try:
            sbc.set_brightness(brightness_level)
            print(f"Setting brightness to {brightness_level}%")
        except Exception as e:
            print("Error setting brightness:", e)
