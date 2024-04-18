from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os


root = Tk()
root.title("TestProgram")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)


def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
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


    icon1 = PhotoImage(file="img/send.png")
    window.iconphoto(False, icon1)

    Sbackground = PhotoImage(file="img/sbackground.png")
    Label(window, image=Sbackground, bg="#f4fdfe", width=440).place(x=0, y=-110)

    Mbackground = PhotoImage(file="img/id.png")
    Label(window, image=Mbackground, bg="#f4fdfe").place(x=-70, y=360)

    host=socket.gethostname()
    Label(window, text=f"ID: {host}", bg='#F8F8F9', fg='black', font=("Acumin Variable Concept", 20, "bold")).place(x=80, y=425)

    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg = "#fff", fg="#000", command=select_file).place(x=160, y=100)
    Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg="#000", fg="#fff", command=sender).place(x=332, y=100)


    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    """
    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()
        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        file = open(filename1, "wb")
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")
    """
    """
    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        try:
            # Attempt to resolve the hostname
            host_ip = socket.gethostbyname(ID)
        except socket.gaierror:
            # Handle invalid hostname
            messagebox.showerror("Error", "Invalid hostname")
            return

        s = socket.socket()
        port = 8080
        try:
            s.connect((host_ip, port))
        except Exception as e:
            # Handle connection error
            messagebox.showerror("Error", f"Error connecting to {ID}: {e}")
            return

        file = open(filename1, "wb")
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")
    """
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

    icon2 = PhotoImage(file="img/receive.png")
    main.iconphoto(False, icon2)

    Hbackground = PhotoImage(file="img/reciever.png")
    Label(main, image=Hbackground, bg="#f4fdfe").place(x=-25,y=0)

    logo = PhotoImage(file="img/profile.png")
    Label(main, image=logo, bg="#f4fdfe").place(x=325,y=365)

    Label(main, text="Receive", font=('arial', 20), bg="#f4fdfe").place(x=175,y=280)

    Label(main, text="Input sender id", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry(main, width=25, fg="black", border=2, bg="white", font=("arial", 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(main, text="filename for the incoming file:", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(main, width=25, fg="black", border=2, bg="white", font=("arial", 15))
    incoming_file.place(x=20, y=450)

    rr = Button(main, text="Receive", width=33, bg="#39c790", font="arial 14 bold", command=receiver)
    rr.place(x=20, y=500)

    main.mainloop()


icon = PhotoImage(file="img/icon.png")
root.iconphoto(False, icon)

Label(root,text="File Transfer",font=("Acumin Variable Concept",20,'bold'),bg="#f4fdfe").place(x=20,y=30)

Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image = PhotoImage(file="img/send.png")
send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
send.place(x=50, y=100)

receive_image = PhotoImage(file="img/receive.png")
receive = Button(root, image=receive_image, bg="#f4fdfe", bd=0, command=Receive)
receive.place(x=300, y=100)

Label(root, text="Send", font=("Acumin Variable Concept", 17, "bold"), bg="#f4fdfe").place(x=67, y=200)
Label(root, text="Receive", font=("Acumin Variable Concept", 17, "bold"), bg="#f4fdfe").place(x=302, y=200)

background = PhotoImage(file="img/background.png")
Label(root, image=background, bg="#f4fdfe").place(x=35, y=320)

root.mainloop()
