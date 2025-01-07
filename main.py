import tkinter as tk
import win32api
import win32con

def adjust_brightness(value):
    print(f"Adjusting brightness to {value}%")
    # Example logic: Adjust the screen brightness (this is a placeholder)
    # Windows doesn't have a direct API for controlling brightness via pywin32
    # This part would interact with a brightness control utility or registry settings
    try:
        # Here, you could use something like WMI or external utilities to actually set brightness
        pass
    except Exception as e:
        print("Error adjusting brightness:", e)

# Set up the main window
root = tk.Tk()
root.title("Dimmer App")
root.geometry("300x100")

# Create a slider for brightness adjustment
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Brightness", command=adjust_brightness)
slider.set(50)  # Start at 50% brightness
slider.pack(pady=20)

# Run the Tkinter loop
root.mainloop()
