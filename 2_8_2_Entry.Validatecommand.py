from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("400x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

import re



def blank_entry():
    phone_entry.delete(0, END)               # удаление введенного текста
    phone_entry.insert(0, tel_blank)         # вставка текста по умолчанию

def is_valid(newval, op):
    result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    if not result and len(newval) <= 12:
        errmsg.set(f"Номер телефона в формате {tel_blank}")
    else:
        errmsg.set("")
    # валидация (focus/focusin/focusout/key)
    if op=="key":
        print("Key")    
    # elif op=="focus":
    #     print("Fokus")
    # elif op=="focusin":
    #     print("Fokusin")
    elif op=="focusout" and len(newval) <= 12:
        print("Fokusout")
        errmsg.set("Необходимо ввести номер телефона")
    if result == "":
        blank_entry()
    return result
    


tel_blank = "+12345678901"

check = (root.register(is_valid), "%P", "%V")
# значение "%V" представляет событие, 
# которое вызывает валидацию (focus/focusin/focusout/key). 
# Тогда в функции валидации с помощью второго параметра мы сможем получить это значение

errmsg = StringVar()
 
phone_entry = ttk.Entry(validate="all", validatecommand=check) 
phone_entry.place(x=5, y=5)

 
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.place(x=140, y=5)

another_entry = ttk.Entry() 
another_entry.place(x=5, y=30)
another_entry.focus()               # устанавоиваем фокус на поле ввода
 

###############################################################################################
root.mainloop()
