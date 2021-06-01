from tkinter import *

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text="Hello world")
label.pack()


def new():
    Toplevel()


button1 = Button(leftframe, text="Button1")
button1.pack(padx=3, pady=3)

button2 = Button(rightframe, text="Button2")
button2.pack(padx=3, pady=3)

button3 = Button(leftframe, text="Button3", command=new)
button3.pack(padx=3, pady=3)

root.title("Test")
root.mainloop()

# import tkinter as tk
#
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello Button"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("Hi there!")
