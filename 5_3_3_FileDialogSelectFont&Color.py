from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

from tkinter import colorchooser

# Выбор шрифта
# значение "configure" указывает, 
# что в данном случае производится настройка диалогового окна. 
# Аргумент "-font" указывает, что следующее значение представляет настройка шрифта, 
# который будет выбран в диалоговом окне по умолчанию. 
# В качестве такового здесь используется шрифт метки label.

# Аргумент "-command" указывает, 
# что дальше идет определение функции, которая будет срабатывать при выборе шрифта. 
# Здесь такой функцией является функция font_changed. 
# Функция выбора шрифта должна принимать один параметр - 
# через него будет передаваться выбранный шрифт. 
# В данном случае просто переустанавливаем шрифт метки.

# Для отображения окна выбора шрифта выполняется вызов
# root.tk.call("tk", "fontchooser", "show")


# Выбор цвета
# Для выбора цвета применяется функции из модуля colorchooser.askcolor():
# Здесь по нажатию на кнопку вызывается функция select_color. 
# В этой функции вызывается функция colorchooser.askcolor. 
# С помощью параметра initialcolor устанавливаем цвет, 
# который выбран по умолчанию в диалоговом окне. 
# В данном случае это черный цвет ("black")

# Результатом функции является кортеж с определениями выбранного цвета. 
# Например, для красного цвета кортеж будет выглядеть следующим образом: 
# ((255, 0, 0), "#ff0000"). То есть, обратившись к второму элементу кортежа, 
# можно получить шестнадцатиричное значение цвета. 
# Здесь выбранный цвет применяется для установки цвета шрифта метки:
# label["foreground"] = result[1]

label = ttk.Label(text="Hello World")
label.pack(anchor=NW, padx=10, pady=10)
 
def font_changed(font):
    label["font"] = font
 
def select_font():
    root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))
    root.tk.call("tk", "fontchooser", "show")

def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    label["foreground"] = result[1]
         

font_button = ttk.Button(text="Выбрать шрифт", command=select_font)
font_button.pack(anchor=NW, padx=10, pady=10)

color_button = ttk.Button(text="Выбрать цвет", command=select_color)
color_button.pack(anchor=NW, padx=10, pady=10)

###############################################################################################
root.mainloop()