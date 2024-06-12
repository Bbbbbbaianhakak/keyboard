import tkinter as tk
from pynput.keyboard import Key, Controller

# Create the main application window
root = tk.Tk()
root.title("Advanced Keyboard")

# Define keyboard layout
keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
    ['Space', 'Enter']
]

# Create a keyboard controller
keyboard = Controller()

# Function to handle key presses
def on_key_press(key):
    if key == 'Space':
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    elif key == 'Enter':
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        keyboard.press(key)
        keyboard.release(key)

# Function to create a button
def create_button(text):
    return tk.Button(root, text=text, width=5, height=2, command=lambda: on_key_press(text))

# Generate buttons for each key in the layout
for row in keys:
    frame = tk.Frame(root)
    frame.pack()
    for key in row:
        button = create_button(key)
        button.pack(side=tk.LEFT)

# Run the application
root.mainloop()
