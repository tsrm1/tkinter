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
    phone_entry.insert(0, blank_text)         # вставка текста по умолчанию

def verifikation_tel(data='', blank_text="", max_lang=12):
    error_code = 0          # всё ОК
    if data == blank_text:
        error_code = 1      # данные совпадают с шаблоном (небыло ввода инфо)
    elif len(data) == 0:
        error_code = 2      # данные отсутствуют
    elif data[0] != "+":
        error_code = 2      # неверный формат данных
    elif len(data)>1:
        if not data[len(data)-1].isdigit():
            error_code = 3  # недопустимые символы при вводе
    if len(data)>max_lang:
        error_code = 4
    # error_code = 0 # всё ОК
    # error_code = 1 # данные совпадают с шаблоном (небыло ввода инфо)
    # error_code = 2 # неверный формат данных
    # error_code = 3 # недопустимые символы при вводе
    return error_code


def is_valid(newval, op):
    print(f'Val={newval}, P={op}')
    error_code = verifikation_tel(data=newval)
    if error_code > 0:
        result = False
        if error_code==1:
            errmsg.set("Введите номер телефона!")
        elif error_code==2 or error_code==3:
            errmsg.set("Формат данных +12345678901")
        elif error_code==4:
            errmsg.set("Достигнута максимальная длинна данных!")
        else:
            errmsg.set("")
    else:
        result = True
        errmsg.set("")

    # валидация (focus/focusin/focusout/key)
    if op=="key":
        pass
    # elif op=="focus":
    #     print("Fokus")
    # elif op=="focusin":
    #     print("Fokusin")
    elif op=="focusout" and len(newval) < 12:
        # print("Fokusout")
        blank_entry()
        errmsg.set("Необходимо ввести номер телефона!")
    return result
    



blank_text=""

phone_entry_check = (root.register(is_valid), "%P", "%V")
# значение "%V" представляет событие, 
# которое вызывает валидацию (focus/focusin/focusout/key). 
# Тогда в функции валидации с помощью второго параметра мы сможем получить это значение

errmsg = StringVar()
 
phone_entry = ttk.Entry(validate="all", validatecommand=phone_entry_check) 
phone_entry.place(x=5, y=5)

 
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.place(x=140, y=5)

another_entry = ttk.Entry() 
another_entry.place(x=5, y=30)
another_entry.focus()               # устанавливаем фокус на поле ввода
 

###############################################################################################
root.mainloop()
