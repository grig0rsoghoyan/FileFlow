from tkinter import *
from tkinter import filedialog
import os

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry("725x522")
    window.configure(bg="#120E20")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(parent=window,
                                              initialdir=os.getcwd(),
                                              title="Select the File")

        # Update the label with the new file name
        if filename != "":
            label.config(text=f"File name: {filename}")
        else:
            label.config(text="No file selected")

    label = Label(window, text="No file selected", bg='#F8F8F9', fg='black', font=("Acumin Variable Concept", 20, "bold"))
    label.place(x=57, y=424)

    select_button = Button(window, text="Select File", command=select_file)
    select_button.place(x=57, y=450)

# Assuming root is defined elsewhere in your code
root = Tk()
Send()
root.mainloop()
