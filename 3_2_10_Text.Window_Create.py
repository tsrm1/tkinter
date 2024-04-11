from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Добавление других виджетов в Text с помощью метода window_create()
# Первый параметр метода window_create также позиция создания виджета, 
# а второй параметр - window указывает на добавляемый виджет, 
# в данном случае это кнопка, на которую также можно нажимать и 
# также можно обрабатывать ее нажатия

editor = Text()
editor.pack(expand=1, fill=BOTH)
 
def click():
    editor.insert("2.0", "Click\n")
 
btn = ttk.Button(editor, text="Click", command=click)
editor.window_create("1.0", window=btn)


###############################################################################################
root.mainloop()
