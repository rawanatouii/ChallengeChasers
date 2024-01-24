import tkinter as tk

# Create the main application window
window = tk.Tk()

# Set the window title
window.title("ChallengeChaser")

# Set the window size
window.geometry("400x300")

# Add a label to the window
label = tk.Label(window, text="Hello!")
label.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
