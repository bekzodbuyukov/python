import tkinter

from cone import Cone
from main_window import MainWindow


if __name__ == "__main__":
    my_cone = Cone(
        radius=10,
        height=22,
        density=14,
        weight=False,
        volume=True
    )

    my_cone.calculate_volume()
    print(round(my_cone.volume, 2))

    root = tkinter.Tk()
    app = MainWindow()
    root.mainloop()

