from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Выделение текста
# Для управления выделением текста виджет Text обладает следующими методами:
# selection_get(): возвращает выделенный фрагмент
# selection_clear(): снимает выделение
# Применим данные методы:

def get_selection():
    label["text"]=editor.selection_get()
 
 
def clear_selection():
    editor.selection_clear()
 
editor = Text(height=5)
editor.pack(fill=X)
 
label = ttk.Label()
label.pack(anchor=NW)
 
get_button = ttk.Button(text="Get selection", command=get_selection)
get_button.pack(side=LEFT)
clear_button = ttk.Button(text="Clear", command=clear_selection)
clear_button.pack(side=RIGHT)


###############################################################################################
root.mainloop()
