from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Добавление изображений и других виджетов
# Виджет Text позволяет добавление изображений и других виджетов.

# Для добавления изображений применяется метод image_create:

editor = Text()
editor.pack(expand=1, fill=BOTH)
 
python_img = PhotoImage(file="./ico/icon2.png")
editor.image_create("1.0", image=python_img)


###############################################################################################
root.mainloop()
