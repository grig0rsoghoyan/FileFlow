from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"img/")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = Tk()
root.title("FileFlow")
root.geometry("725x522")
root.configure(bg = "#110D20")
root.resizable(False, False)

canvas = Canvas(
    root,
    bg = "#110D20",
    height = 522,
    width = 725,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


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
                                              title="Select the File", )

    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        print(f"Server started on {host}:{port}")
        s.listen(1)  # Listen for incoming connections, with a backlog of 1
        print("Waiting for any incoming connections...")
        conn, addr = s.accept()
        file = open(filename, "rb")
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")

    icon = PhotoImage(file="img/icon.png")
    window.iconphoto(False, icon)

    canvas1 = Canvas(
        window,
        bg="#120E20",
        height=522,
        width=725,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas1.place(x=0, y=0)
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_3 = canvas1.create_image(
        362.0,
        117.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_4 = canvas1.create_image(
        131.0,
        91.0,
        image=image_image_4
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_send.png"))
    button_1 = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=sender,
        relief="flat"
    )
    button_1.place(
        x=495.0,
        y=160.0,
        width=192.0,
        height=202.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_upload.png"))
    button_2 = Button(
        window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=select_file,
        relief="flat"
    )
    button_2.place(
        x=47.0,
        y=161.0,
        width=413.0,
        height=201.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_5 = canvas1.create_image(
        367.0,
        442.0,
        image=image_image_5
    )

    host = socket.gethostname()
    Label(window, text=f"ID: {host}", bg='#F8F8F9', fg='black', font=("Acumin Variable Concept", 20, "bold")).place(x=57, y=424)

    window.mainloop()


def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry("725x522")
    main.configure(bg="#120E20")
    main.resizable(False, False)

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        try:
            # Attempt to resolve the hostname
            host_ip = socket.gethostbyname(ID)
        except socket.gaierror as e:
            # Handle invalid hostname
            messagebox.showerror("Error", f"Invalid hostname: {e}")
            return

        try:
            s = socket.socket()
            port = 8080
            s.connect((host_ip, port))
        except Exception as e:
            # Handle connection error
            messagebox.showerror("Error", f"Error connecting to {ID}: {e}")
            return

        file = open(filename1, "wb")
        while True:
            file_data = s.recv(1024)
            if not file_data:
                break
            file.write(file_data)
        file.close()
        print("File has been received successfully")

    icon = PhotoImage(file="img/icon.png")
    main.iconphoto(False, icon)

    canvas2 = Canvas(
        main,
        bg="#120E20",
        height=522,
        width=725,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas2.place(x=0, y=0)
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
    SenderID = Entry(
        main,
        bd=0,
        bg="#120E20",
        fg="#ffffff",
        highlightthickness=0
    )
    SenderID.place(
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
    incoming_file = Entry(
        main,
        bd=0,
        bg="#120E20",
        fg="#ffffff",
        highlightthickness=0
    )
    incoming_file.place(
        x=159.0,
        y=325.0,
        width=379.0,
        height=44.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_receive.png"))
    button_1 = Button(
        main,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=receiver,
        relief="flat"
    )
    button_1.place(
        x=223.0,
        y=416.0,
        width=279.0,
        height=57.0
    )

    main.mainloop()


icon = PhotoImage(file="img/icon.png")
root.iconphoto(False, icon)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_bg.png"))
image_1 = canvas.create_image(
    304.0,
    431.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_title.png"))
image_2 = canvas.create_image(
    362.0,
    133.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_send0.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=Send,
    relief="flat"
)
button_1.place(
    x=44.0,
    y=241.0,
    width=297.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_receive0.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Receive,
    relief="flat"
)
button_2.place(
    x=384.0,
    y=241.0,
    width=297.0,
    height=65.0
)


root.mainloop()