from tkinter import BOTH, Menu, Scrollbar, Text, RIGHT, Y, Tk, END
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def cut():
    TextArea.event_generate("<>")


def copy():
    TextArea.event_generate("<>")


def paste():
    TextArea.event_generate("<>")


def about():
    showinfo("Notepad", "A Simple Notepad")


root = Tk()
root.title("Untitled - Notepad")
root.wm_iconbitmap("icon.ico")
root.geometry("1024x724")

TextArea = Text(root, font="arial_black 20")
file = None
TextArea.pack(expand=True, fill=BOTH)

MenuBar = Menu(root)

FileMenu = Menu(MenuBar, tearoff=0, bg="black", fg="green", font="15")
FileMenu.add_command(label="New", command=newfile)
FileMenu.add_command(label="Open", command=openfile)
FileMenu.add_command(label="Save", command=savefile)
MenuBar.add_cascade(label="File", menu=FileMenu)

EditMenu = Menu(MenuBar, tearoff=0, bg="black", fg="green", font="15", bd="0")
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
MenuBar.add_cascade(label="Edit", menu=EditMenu)

HelpMenu = Menu(MenuBar, tearoff=0, bg="black", fg="green", font="15")
HelpMenu.add_command(label="About Notepad", command=about, bitmap="warning")
MenuBar.add_cascade(label="Help", menu=HelpMenu, compound=RIGHT)

root.config(menu=MenuBar)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
