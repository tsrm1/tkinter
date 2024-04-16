from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("700x700+100+100")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Создание прокрутки
# Для создания прокрутки виджет Canvas предоставляет параметр, 
# который позволяет установить прокручиваемую область:

h = ttk.Scrollbar(orient=HORIZONTAL)
v = ttk.Scrollbar(orient=VERTICAL)
canvas = Canvas(scrollregion=(0, 0, 1400, 1400), bg="white", yscrollcommand=v.set, xscrollcommand=h.set)
h["command"] = canvas.xview
v["command"] = canvas.yview
 
canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
 
canvas.create_rectangle(10,10, 300, 300, fill="red")

###############################################################################################
root.mainloop()