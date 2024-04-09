from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

def select():
    result = "Выбрано: "
    if python.get() == 1: result = f"{result} Python"
    if javascript.get() == 1: result = f"{result} JavaScript"
    if java.get() == 1: result = f"{result} Java"
    languages.set(result)
 
position = {"padx":6, "pady":6, "anchor":NW}
 
languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)
 
python = IntVar()
python_checkbutton = ttk.Checkbutton(text="Python", variable=python, command=select)
python_checkbutton.pack(**position)
 
javascript = IntVar()
javascript_checkbutton = ttk.Checkbutton(text="JavaScript", variable=javascript, command=select)
javascript_checkbutton.pack(**position)
 
java = IntVar()
java_checkbutton = ttk.Checkbutton(text="Java", variable=java, command=select)
java_checkbutton.pack(**position)





###############################################################################################
root.mainloop()
