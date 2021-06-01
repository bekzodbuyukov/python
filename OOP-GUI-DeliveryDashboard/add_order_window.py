import tkinter as tk
import tkinter.font as font

from delivery_order import DeliveryOrder


class AddOrderWindow(tk.Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.grid()
        self.text_font = font.Font(self, family="Poppins")
        # Labels and Buttons
        self.distance_label = tk.Label(self)
        self.distance_entry = tk.Entry(self)
        self.product_name_label = tk.Label(self)
        self.product_name_entry = tk.Entry(self)
        self.delivery_date_label = tk.Label(self)
        self.delivery_date_entry = tk.Entry(self)
        self.car_number_label = tk.Label(self)
        self.car_number_entry = tk.Entry(self)
        self.save_button = tk.Button(self)
        self.go_back_button = tk.Button(self)
        self.buttons = []
        # All About Order
        self.distance = None
        self.product_name = None
        self.delivery_date = None
        self.car_number = None
        self.orders = []
        self.order_status_label = tk.Label(self)
        self.successfully_added_label = tk.Label(self)
        self.show_window()

    def show_window(self) -> None:
        self.distance_label["text"] = "Distance (km):"
        self.distance_label.grid({"row": 0, "padx": 10,
                                  "pady": 10})
        self.distance_entry.grid({"row": 0, "column": 1,
                                  "padx": 10, "pady": 10})

        self.product_name_label["text"] = "Product name:"
        self.product_name_label.grid({"row": 1, "padx": 10,
                                      "pady": 10})
        self.product_name_entry.grid({"row": 1, "column": 1,
                                      "padx": 10, "pady": 10})

        self.delivery_date_label["text"] = "Delivery date:"
        self.delivery_date_label.grid({"row": 2, "padx": 10, "pady": 10})
        self.delivery_date_entry.grid({"row": 2, "column": 1,
                                       "padx": 10, "pady": 10})

        self.car_number_label["text"] = "Car number:"
        self.car_number_label.grid({"row": 3, "padx": 10, "pady": 10})
        self.car_number_entry.grid({"row": 3, "column": 1,
                                    "padx": 10, "pady": 10})

        self.order_status_label["text"] = "Order Status:"
        self.order_status_label.grid({"row": 4, "column": 0,
                                      "padx": 10, "pady": 10})

        self.successfully_added_label["text"] = "New"
        self.successfully_added_label["foreground"] = "blue"
        self.successfully_added_label.grid({"row": 4, "column": 1,
                                            "padx": 10, "pady": 10})

        self.go_back_button["text"] = "Go Back"
        self.go_back_button["command"] = self.destroy
        self.go_back_button.grid({"row": 5, "column": 0})
        self.buttons.append(self.go_back_button)

        self.save_button["text"] = "Save"
        self.save_button["command"] = self.save_order
        self.save_button.grid({"row": 5, "column": 1})
        self.buttons.append(self.save_button)

        for button in self.buttons:
            button["fg"] = "black"
            button["font"] = self.text_font
            button["activebackground"] = "black"
            button["activeforeground"] = "white"
            button.grid({"padx": 10, "pady": 10})

    def save_order(self):
        self.distance = self.distance_entry.get()
        self.product_name = self.product_name_entry.get()
        self.delivery_date = self.delivery_date_entry.get()
        self.car_number = self.car_number_entry.get()

        new_order = DeliveryOrder(
            distance=int(self.distance),
            name=self.product_name,
            date=self.delivery_date,
            car_number=self.car_number
        )
        self.orders.append(new_order)

        self.distance_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)
        self.delivery_date_entry.delete(0, tk.END)
        self.car_number_entry.delete(0, tk.END)

        self.successfully_added_label["text"] = "[+] Successfully added"
        self.successfully_added_label["foreground"] = "green"
        self.successfully_added_label.grid({"row": 4, "column": 1,
                                            "padx": 10, "pady": 10})

        print(new_order)
