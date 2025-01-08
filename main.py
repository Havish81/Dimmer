import tkinter as tk
from systemBrightness import SystemBrightness

# Create an instance of the brightness controller
brightness_controller = SystemBrightness()

def adjust_brightness(value):
    try:
        brightness_level = int(value)
        print(f"Adjusting brightness to: {brightness_level}%")
        brightness_controller.set_brightness(brightness_level)
    except Exception as e:
        print("Error adjusting brightness:", e)

# Function to set the slider to the current system brightness
def set_initial_brightness():
    try:
        current_brightness = brightness_controller.get_brightness()
        slider.set(current_brightness)  # Set slider to current system brightness
    except Exception as e:
        print("Error getting initial brightness:", e)

# Set up the main window
root = tk.Tk()
root.title("Dimmer App")
root.geometry("400x150")
root.configure(bg="grey")  # Default background color

# Function to change background color based on slider value
def update_background(value):
    if int(value) >= 0:
        root.configure(bg="grey")  # Regular mode color
    elif int(value) < 0:
        root.configure(bg="darkred")  # Super Dark Mode color for negative range

# Create a slider for brightness adjustment (from -30 to 100)
slider = tk.Scale(root, from_=-30, to=100, orient="horizontal", 
                  label="Brightness", command=adjust_brightness, 
                  sliderrelief="raised", troughcolor="gray",
                  fg="white", bg="black")

# Change color of the slider's negative range (-1 to -30) to red
slider.config(highlightbackground="red", foreground="white", background="black")

# Set the slider to the current system brightness on launch
set_initial_brightness()

slider.pack(pady=20)

# Attach the background color change to the slider
slider.bind("<Motion>", lambda e: update_background(slider.get()))

# Run the Tkinter loop
root.mainloop()
