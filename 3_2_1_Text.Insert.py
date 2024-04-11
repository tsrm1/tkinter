from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
 
editor = Text(wrap = "none")
editor.grid(column = 0, row = 0, sticky = NSEW)
 
ys = ttk.Scrollbar(orient = "vertical", command = editor.yview)
ys.grid(column = 1, row = 0, sticky = NS)
xs = ttk.Scrollbar(orient = "horizontal", command = editor.xview)
xs.grid(column = 0, row = 1, sticky = EW)
 
editor["yscrollcommand"] = ys.set
editor["xscrollcommand"] = xs.set

###############################################################################################

# Добавление текста
# Для добавления текста применяется метод insert():
editor.insert("1.0", "Hello World")     # вставка в начало
editor.insert(END, "\nBye World")       # вставка в конец


###############################################################################################
root.mainloop()

