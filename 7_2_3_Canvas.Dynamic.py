from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("700x700+100+100")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# изменим цвет линии
red = "red"
blue= "blue"
 
selected_color = StringVar(value=red)
 
canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(anchor=CENTER, expand=1)
 
def select():
    canvas.itemconfigure(line, fill=selected_color.get())
 
red_btn = ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6)
red_btn.pack(anchor=NW)
blue_btn = ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6)
blue_btn.pack(anchor=NW)
 
line = canvas.create_line(10, 10, 200, 100, fill=selected_color.get())

###############################################################################################
root.mainloop()