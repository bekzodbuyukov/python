import tkinter as tk
import tkinter.font as font

from window import Window
from add_order_window import AddOrderWindow
from get_orders_window import GetOrdersWindow


class MainWindow(Window):
    def __init__(self) -> None:
        super().__init__(header_name=" Delivery Dashboard")
        self.text_font = font.Font(self, family="Poppins")
        # Buttons
        self.add_order_button = tk.Button(self)
        self.get_orders_button = tk.Button(self)
        self.about_button = tk.Button(self)
        self.quit_button = tk.Button(self)
        self.buttons = []
        self.grid()
        self.show_buttons()

    def add_orders_data(self) -> None:
        orders = AddOrderWindow()
        self.all_orders = orders.orders

    def get_orders_table(self) -> None:
        GetOrdersWindow(orders=self.all_orders)

    def show_buttons(self) -> None:
        self.add_order_button["text"] = "Add Order"
        self.add_order_button["command"] = self.add_orders_data
        self.add_order_button.grid({"row": 0, "column": 0})

        self.get_orders_button["text"] = "Get Orders"
        self.get_orders_button["command"] = self.get_orders_table
        self.get_orders_button.grid({"row": 0, "column": 1})

        self.about_button["text"] = "About"
        self.about_button["command"] = self.show_about_window
        self.about_button.grid({"row": 1, "column": 0})

        self.quit_button["text"] = "Quit"
        self.quit_button["command"] = self.destroy
        self.quit_button.grid({"row": 1, "column": 1})

        self.buttons = [self.add_order_button, self.get_orders_button,
                        self.about_button, self.quit_button]

        for button in self.buttons:
            button["fg"] = "black"
            button["font"] = self.text_font
            button["activebackground"] = "black"
            button["activeforeground"] = "white"
            button.grid({"padx": 10, "pady": 10})

    def show_about_window(self) -> None:
        about_window = tk.Toplevel()
        about_window.grid()

        about_label = tk.Label(about_window, text="Developed by: Bekzod Buyukov\n"
                                                  "(c) Copyifyouwant 2021\n"
                                                  "University Task\n",
                               cnf={"font": self.text_font})
        about_label.grid({"row": 0, "padx": 10, "pady": 10})

        go_back_button = tk.Button(about_window, text="Go Back")
        go_back_button["command"] = about_window.destroy
        go_back_button["fg"] = "black"
        go_back_button["font"] = self.text_font
        go_back_button["activebackground"] = "black"
        go_back_button["activeforeground"] = "white"
        go_back_button.grid({"row": 1, "column": 0, "padx": 10, "pady": 10})
