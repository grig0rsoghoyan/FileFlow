from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

def open_root():
    root = Tk()
    root.title("FileFlow")
    root.geometry("725x522")
    root.configure(bg="#FFFFFF")
    root.resizable(False, False)

    canvas = Canvas(
        root,
        bg="#FFFFFF",
        height=522,
        width=725,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    def Send():
        root.destroy()  # Close the current window
        SendWindow()

    def Receive():
        root.destroy()  # Close the current window
        ReceiveWindow()


    icon = PhotoImage(file="img/icon.png")
    root.iconphoto(False, icon)

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        1275.0,
        184.0000056040464,
        3831.0,
        186.00022888183594,
        fill="#000000",
        outline="")

    canvas.create_text(
        195.0,
        49.0,
        anchor="nw",
        text="FileFlow",
        fill="#000000",
        font=("ArimoHebrewSubsetItalic Italic", 96 * -1)
    )

    button_image_1 = PhotoImage(
        file="img/send.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Send,
        relief="flat",
        bg="#ffffff"
    )
    button_1.place(
        x=111.0,
        y=232.0,
        width=329.1266174316406,
        height=101.582275390625
    )

    button_image_2 = PhotoImage(
        file="img/receive.png")
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Receive,
        relief="flat",
        bg="#ffffff"
    )
    button_2.place(
        x=275.0,
        y=362.0,
        width=329.1266174316406,
        height=101.582275390625
    )

    root.mainloop()

def SendWindow():
    window = Toplevel()
    window.title("Send")
    window.geometry("725x522")
    window.configure(bg="#FFFFFF")
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

    def HomeFromSend():
        window.destroy()  # Close the current window
        open_root()

    icon1 = PhotoImage(file="img/send.png")
    window.iconphoto(False, icon1)

    canvas1 = Canvas(
        window,
        bg="#FFFFFF",
        height=522,
        width=725,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas1.place(x=0, y=0)
    canvas1.create_text(
        14.0,
        9.0,
        anchor="nw",
        text="Send the file",
        fill="#000000",
        font=("ArimoHebrewSubsetItalic Italic", 48 * -1)
    )

    button_image_3 = PhotoImage(
        file="img/button_1.png")
    button_3 = Button(
        window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=sender,
        relief="flat",
        bg="#ffffff"
    )
    button_3.place(
        x=502.0,
        y=90.0,
        width=204.13424682617188,
        height=274.0
    )

    button_image_4 = PhotoImage(
        file="img/button_2.png")
    button_4 = Button(
        window,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=select_file,
        relief="flat",
        bg="#ffffff"
    )
    button_4.place(
        x=14.0,
        y=90.0,
        width=470.0,
        height=274.0
    )

    button_image_6 = PhotoImage(
        file="img/entry_1.png")
    button_6 = Button(
        window,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=HomeFromSend(),
        relief="flat",
        bg="#ffffff"
    )
    button_6.place(
        x=140.0,
        y=200.0,
        width=470.0,
        height=274.0
    )

    host = socket.gethostname()
    Label(window, text=f"ID: {host}", bg='#F8F8F9', fg='black', font=("Acumin Variable Concept", 20, "bold")).place(x=17, y=394)

    window.mainloop()

def ReceiveWindow():
    main = Toplevel()
    main.title("Receive")
    main.geometry("725x522")
    main.configure(bg="#FFFFFF")
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

    def HomeFromReceive():
        main.destroy()  # Close the current window
        open_root()

    icon2 = PhotoImage(file="img/receive.png")
    main.iconphoto(False, icon2)

    canvas3 = Canvas(
        main,
        bg="#FFFFFF",
        height=522,
        width=725,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas3.place(x=0, y=0)
    canvas3.create_text(
        14.0,
        9.0,
        anchor="nw",
        text="Receive files",
        fill="#000000",
        font=("ArimoHebrewSubsetItalic Italic", 64 * -1)
    )

    canvas3.create_text(
        14.0,
        123.0,
        anchor="nw",
        text="Input sender ID",
        fill="#000000",
        font=("JuliusSansOne Regular", 48 * -1)
    )

    entry_image_1 = PhotoImage(
        file="img/entry_1.png")
    entry_bg_1 = canvas3.create_image(
        344.5,
        203.5,
        image=entry_image_1
    )
    SenderID = Entry(
        main,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    SenderID.place(
        x=34.5,
        y=184.0,
        width=620.0,
        height=37.0
    )

    canvas3.create_text(
        14.0,
        251.0,
        anchor="nw",
        text="Filename for the incoming file",
        fill="#000000",
        font=("JuliusSansOne Regular", 40 * -1)
    )

    entry_image_2 = PhotoImage(
        file="img/entry_2.png")
    entry_bg_2 = canvas3.create_image(
        344.5,
        328.5,
        image=entry_image_2
    )
    incoming_file = Entry(
        main,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    incoming_file.place(
        x=34.5,
        y=309.0,
        width=620.0,
        height=37.0
    )

    button_image_5 = PhotoImage(
        file="img/button_3.png")
    button_5 = Button(
        main,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=receiver,
        relief="flat",
        bg="#ffffff"
    )
    button_5.place(
        x=15.0,
        y=380.0,
        width=667.0,
        height=98.0
    )

    main.mainloop()

open_root()
