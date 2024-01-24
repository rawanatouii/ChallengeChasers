import tkinter as tk

# Create the main application window
window = tk.Tk()

# Set the window title
window.title("ChallengeChaser")

# Set the window size
window.geometry("400x300")
#set the window's background color
window.configure(bg="black")

def resize(event):
    # Get the new size of the window
    new_width = event.width
    new_height = event.height
       # Resize the image
    resized_image = image.subsample(int(image.width() / new_width), int(image.height() / new_height))

    # Update the image label
    logo.config(image=resized_image)
    logo.image = resized_image
    logo.place(relx=0.5, rely=0.5, anchor="center")

logo = ".\photos\Logo_challenge.png"  # Replace with the actual path to your image
image = tk.PhotoImage(file=logo)

logo =tk.Label(window, image=image, bg="black")
logo.image = image
logo.place(relx=0.5, rely=0.5, anchor="center")
# Bind the resize function to the window's configure event
window.bind("<Configure>", resize)
# Start the Tkinter event loop
window.mainloop()
