import tkinter as tk


class Window(tk.Tk):
    def __init__(self, header_name: str) -> None:
        super().__init__(className=header_name)

    def __repr__(self) -> str:
        return "Window Template"
