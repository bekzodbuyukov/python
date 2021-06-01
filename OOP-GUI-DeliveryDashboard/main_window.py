import tkinter as tk
import tkinter.font as font

from window import Window


class MainWindow(Window):
    def __init__(self) -> None:
        super().__init__(header_name=" Delivery Dashboard")
        self.text_font = font.Font(self, family="Poppins")
        self.add_order_button = tk.Button(self)
        self.get_orders_button = tk.Button(self)
        self.about_button = tk.Button(self)
        self.quit_button = tk.Button(self)
        self.buttons = []
        self.grid()
        self.show_buttons()

    def show_buttons(self):
        self.add_order_button["text"] = "Add Order"
        self.add_order_button.grid({"row": 0, "column": 0})
        self.buttons.append(self.add_order_button)

        self.get_orders_button["text"] = "Get Orders"
        self.get_orders_button.grid({"row": 0, "column": 1})
        self.buttons.append(self.get_orders_button)

        self.about_button["text"] = "About"
        self.about_button["command"] = self.show_about_window
        self.about_button.grid({"row": 1, "column": 0})
        self.buttons.append(self.about_button)

        self.quit_button["text"] = "Quit"
        self.quit_button["command"] = self.destroy
        self.quit_button.grid({"row": 1, "column": 1})
        self.buttons.append(self.quit_button)

        for button in self.buttons:
            button["fg"] = "black"
            button["font"] = self.text_font
            button["activebackground"] = "black"
            button["activeforeground"] = "white"
            button.grid({"padx": 10, "pady": 10})

    def show_about_window(self):
        about_window = tk.Toplevel()
        about_window.grid()

        about_label = tk.Label(about_window, text="Developed by: Bekzod Buyukov\n"
                                                  "(c) Copyifyouwant 2021\n"
                                                  "University Task\n")
        about_label.grid({"row": 0, "padx": 10, "pady": 10})

        go_back_button = tk.Button(about_window, text="Go Back")
        go_back_button["command"] = about_window.destroy
        go_back_button["fg"] = "black"
        go_back_button["font"] = self.text_font
        go_back_button["activebackground"] = "black"
        go_back_button["activeforeground"] = "white"
        go_back_button.grid({"row": 1, "padx": 10, "pady": 10})
