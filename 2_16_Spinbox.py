from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Виджет Spinbox позволяет выбрать значение (чаще число) из некоторого списка.
# Основные параметры Spinbox:
# values: набор значений виджета в виде списка или кортежа
# from_: минимальное значение (тип float)
# to: максимальное значение (тип float)
# increment: приращение значения (тип float)
# textvariable: определяет переменную StringVar, которая хранит текущее значение виджета
# command: указывает на функцию, которая вызывается при изменении значения виджета
# wrap: при значении True создает зацикленный список, при котором после минимального значения идет максимальное.
# background: фоновый цвет
# foreground: цвет текста
# font: шрифт виджета
# justify: выравнивание текста, принимает значения "left" (по левому краю), "right" (по правому краю) и "center" (по центру)
# width: ширина виджета
# state: состояние виджета


spinbox = ttk.Spinbox(from_=1.0, to=100.0)
spinbox.pack(anchor=NW)
###############################################################################################

# запретить ручной ввод значений в текстовое поле
spinbox = ttk.Spinbox(from_=1.0, to=100.0, state="readonly") 
spinbox.pack(anchor=NW)

###############################################################################################

# increment: приращение значения (тип float)
spinbox = ttk.Spinbox(from_=0.0, to=100.0, increment=5) 
spinbox.pack(anchor=NW)

###############################################################################################

# С помощью параметра textvariable можно привязать значение Spinbox к переменной StringVar:
spinbox_var = StringVar(value=22) # начальное значение 22
 
label = ttk.Label(textvariable=spinbox_var)
label.pack(anchor=NW)
 
spinbox = ttk.Spinbox(from_=1.0, to=100.0, textvariable=spinbox_var)
spinbox.pack(anchor=NW)

###############################################################################################

# Обработка изменения значения
# Чтобы обработать изменение значения нужно определить функцию, 
# которая будет срабатывать при изменении значения, 
# и передать ее параметру command:
def change():
    label["text"] = spinbox.get()
 
label = ttk.Label()
label.pack(anchor=NW)
 
spinbox = ttk.Spinbox(from_=0.0, to=100.0, command=change)
spinbox.pack(anchor=NW)

###############################################################################################

# Установка набора значений
# это может быть любой набор значений в виде списка или кортежа, 
# который можно установить с помощью параметра values:
spinbox_var = StringVar()
 
languages=["Python", "JavaScript", "C#", "Java", "C++"]
 
label = ttk.Label(textvariable=spinbox_var)
label.pack(anchor=NW)
 
spinbox = ttk.Spinbox(textvariable=spinbox_var, values=languages)
spinbox.pack(anchor=NW)




###############################################################################################
root.mainloop()
