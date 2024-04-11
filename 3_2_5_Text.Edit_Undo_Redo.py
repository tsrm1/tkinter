from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Повтор и отмена операций
# Методы edit_undo() и edit_redo() позволяют соответственно отменить и повторить операцию 
# (добавление, изменение, удаление текста). 
# Данные методы применяются, если в виджете Text параметр undo равен True. 
# Стоит отметить, что данные методы оперируют своим стеком операций, 
# в котором сохраняются данные операций. 
# Однако если стек для соответствующего метода пуст, 
# то вызов метода вызывает исключение. Простейший пример, 
# где по нажатию на кнопку вызывается отмена или возврат операции:

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)
 
editor = Text(undo=True)
editor.grid(column = 0, columnspan=2, row = 0, sticky = NSEW)
 
def undo():
    editor.edit_undo()
 
def redo():
    editor.edit_redo()
 
redo_button = ttk.Button(text="Undo", command=undo)
redo_button.grid(column=0, row=1)
clear_button = ttk.Button(text="Redo", command=redo)
clear_button.grid(column=1, row=1)

###############################################################################################
root.mainloop()

