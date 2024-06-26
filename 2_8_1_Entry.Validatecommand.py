from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x350+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

import re
 
def is_valid(newval):
    result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    print(result)
    if not result and len(newval) <= 12:
        errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    else:
        errmsg.set("")
    return result
 
check = (root.register(is_valid), "%P")
 
errmsg = StringVar()
 
phone_entry = ttk.Entry(validate="key", validatecommand=check) 
phone_entry.pack(padx=5, pady=5, anchor=NW)
 
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(padx=5, pady=5, anchor=NW)


###############################################################################################
root.mainloop()
