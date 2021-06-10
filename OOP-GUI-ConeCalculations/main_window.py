from tkinter import Frame, Menu


class MainWindow(Frame):
    def __init__(self):
        super().__init__()
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        self.file_menu = Menu(self.menu_bar)
        self.show_window()

    def show_window(self):
        self.master.title("Cone Calculations App")

        self.file_menu.add_command(label="Exit", command=self.exit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

    def exit(self):
        self.quit()
