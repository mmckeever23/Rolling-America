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

# Board and title elements
board_path = 'board.png'
board_image = tk.PhotoImage(file=board_path)
board = tk.Label(root, image=board_image)
board.place(x=f'{x}', y=f'{y}')
title = ttk.Label(root, text="Rolling America", font=('Magneto', 50))
title.pack()

# Combobox choices
combo1_choice = ctk.StringVar()

dice_values = [1, 2, 3, 4, 5, 6]

combo1 = ttk.Combobox(root, values=dice_values, width=2, justify="center", textvariable=combo1_choice, state="readonly")

combo1.place(x=267, y=165)

b1 = ctk.CTkButton(root, text="New Game")
b1.pack(padx=5, pady=10)

root.mainloop()
