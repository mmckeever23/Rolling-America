import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
from ttkbootstrap.constants import *

root = tk.Tk()
root.title("Rolling America")
app_width = 1484
app_height = 864
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))
root.geometry(f'{screen_width}x{screen_height}')


board_path = 'board.png'
board_image = tk.PhotoImage(file=board_path)

board = tk.Label(root, image=board_image)
board.place(x=f'{x}', y=f'{y}')

title = ttk.Label(root, text="Rolling America", font=('Magneto', 50))
title.pack()

b1 = ctk.CTkButton(root, text="Button 1")
b1.pack(padx=5, pady=10)

b2 = ctk.CTkButton(root, text="Button 2")
b2.pack(padx=5, pady=10)

root.mainloop()
