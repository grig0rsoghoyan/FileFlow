
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"img/")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


main = Tk()

main.geometry("725x522")
main.configure(bg ="#120E20")


canvas2 = Canvas(
    main,
    bg = "#120E20",
    height = 522,
    width = 725,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas2.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_bg1.png"))
image_1 = canvas2.create_image(
    311.0,
    411.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_title1.png"))
image_2 = canvas2.create_image(
    149.0,
    74.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_rct.png"))
image_3 = canvas2.create_image(
    362.0,
    259.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_title0.png"))
image_4 = canvas2.create_image(
    363.0,
    157.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_id.png"))
image_5 = canvas2.create_image(
    259.0,
    213.0,
    image=image_image_5
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_id.png"))
entry_bg_1 = canvas2.create_image(
    348.5,
    258.0,
    image=entry_image_1,
)
entry_1 = Entry(
    bd=0,
    bg="#120E20",
    fg="#ffffff",
    highlightthickness=0
)
entry_1.place(
    x=159.0,
    y=235.0,
    width=379.0,
    height=44.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_filename.png"))
image_6 = canvas2.create_image(
    332.0,
    303.0,
    image=image_image_6
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_filename.png"))
entry_bg_2 = canvas2.create_image(
    348.5,
    348.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#120E20",
    fg="#ffffff",
    highlightthickness=0
)
entry_2.place(
    x=159.0,
    y=325.0,
    width=379.0,
    height=44.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_receive.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_receive clicked"),
    relief="flat"
)
button_1.place(
    x=223.0,
    y=416.0,
    width=279.0,
    height=57.0
)
main.resizable(False, False)
main.mainloop()
