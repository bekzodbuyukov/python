import tkinter as tk
import tkinter.font as font


class GetOrdersWindow(tk.Toplevel):
    def __init__(self, orders: iter) -> None:
        super().__init__()
        self.grid()
        self.orders_list = orders
        self.text_font = font.Font(self, family="Poppins")
        # Labels and Buttons
        self.counting_column_label = tk.Label(self, {"font": self.text_font})
        self.distance_column_label = tk.Label(self, {"font": self.text_font})
        self.product_name_column_label = tk.Label(self, {"font": self.text_font})
        self.delivery_date_column_label = tk.Label(self, {"font": self.text_font})
        self.car_number_column_label = tk.Label(self, {"font": self.text_font})
        self.go_back_button = tk.Button(self, {"font": self.text_font})
        self.show_orders_details()

    def set_orders_list(self, orders: iter) -> None:
        self.orders_list.extend(orders)

    def show_orders_details(self) -> None:
        self.counting_column_label["text"] = "#"
        self.counting_column_label.grid({"row": 0, "column": 0,
                                         "padx": 10, "pady": 10})

        self.distance_column_label["text"] = "Distance"
        self.distance_column_label.grid({"row": 0, "column": 1,
                                         "padx": 10, "pady": 10})

        self.product_name_column_label["text"] = "Product name"
        self.product_name_column_label.grid({"row": 0, "column": 2,
                                             "padx": 10, "pady": 10})

        self.delivery_date_column_label["text"] = "Delivery date"
        self.delivery_date_column_label.grid({"row": 0, "column": 3,
                                              "padx": 10, "pady": 10})

        self.car_number_column_label["text"] = "Car number"
        self.car_number_column_label.grid({"row": 0, "column": 4,
                                           "padx": 10, "pady": 10})

        for index, order in enumerate(self.orders_list):
            row = 2 + index
            column = 0

            counting_column = tk.Label(self, text=str(index + 1))
            distance_column = tk.Label(self, text=order.distance)
            product_name_column = tk.Label(self, text=order.product_name)
            delivery_date_column = tk.Label(self, text=order.delivery_date)
            car_number_column = tk.Label(self, text=order.car_number)

            table_columns = [counting_column, distance_column,
                             product_name_column, delivery_date_column,
                             car_number_column]

            for column_index, table_column in enumerate(table_columns):
                table_column.grid({"row": row,
                                  "column": column + column_index,
                                   "padx": 10, "pady": 10})

        self.go_back_button["text"] = "Go Back"
        self.go_back_button["command"] = self.destroy
        self.go_back_button["fg"] = "black"
        self.go_back_button["font"] = self.text_font
        self.go_back_button["activebackground"] = "black"
        self.go_back_button["activeforeground"] = "white"
        self.go_back_button.grid({"row": len(self.orders_list) + 2,
                                  "padx": 10, "pady": 10})
