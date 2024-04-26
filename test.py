import tkinter as tk

def rounded_button_click():
    print("Rounded button clicked")

# Function to create a rounded button
def create_rounded_button(canvas, x, y, width, height, radius, text, command):
    button = tk.Button(
        master=canvas,
        text=text,
        command=command,
        relief=tk.FLAT,
        bg="#303030",
        fg="white",
        font=("Arial", 12)
    )

    # Create rounded rectangle background
    canvas.create_oval(x, y, x+radius*2, y+radius*2, fill="#303030")
    canvas.create_oval(x+width-radius*2, y, x+width, y+radius*2, fill="#303030")
    canvas.create_oval(x, y+height-radius*2, x+radius*2, y+height, fill="#303030")
    canvas.create_oval(x+width-radius*2, y+height-radius*2, x+width, y+height, fill="#303030")
    canvas.create_rectangle(x+radius, y, x+width-radius, y+height, fill="#303030")
    canvas.create_rectangle(x, y+radius, x+width, y+height-radius, fill="#303030")

    # Place the button text
    button_window = canvas.create_window(
        x + width / 2,
        y + height / 2,
        anchor=tk.CENTER,
        window=button
    )

# Create the main main
window = tk.Tk()
window.geometry("400x200")
window.configure(bg="#110D20")

canvas = tk.Canvas(
    window,
    bg="#110D20",
    height=200,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Create the rounded button
create_rounded_button(canvas, 100, 50, 200, 50, 20, "Click Me", rounded_button_click)

window.mainloop()
