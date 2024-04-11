from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# # Виджет Text
# # Text предназначен для отображения и редактирования многострочного текста. Стоит отметить, что данный виджет доступен только в основном пакете tkinter, в пакете tkinter.ttk аналога нет.
# # Основные параметры конструктора Text:
# # bd / borderwidth: толщина границы
# # bg/background: фоновый цвет
# # fg/foreground: цвет текста
# # font: шрифт текста, например, font="Arial 14" - шрифт Arial высотой 14px, или font=("Verdana", 13, "bold") - шрифт Verdana высотой 13px с выделением жирным
# # height: высота в строках
# # padx: отступ от границ кнопки до ее текста справа и слева
# # pady: отступ от границ кнопки до ее текста сверху и снизу
# # relief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE
# # state: устанавливает состояние кнопки, может принимать значения DISABLED, ACTIVE, NORMAL (по умолчанию)
# # width: ширина в символах
# # wrap: указывает, каким образом переносить текст, если он не вмещается в границы виджета


# editor = Text()
# editor.pack(fill=BOTH, expand=1)

###############################################################################################

# # Перенос текста
# # стратегия переноса, которая устанавливается с помощью параметра wrap. 
# # Этот параметр может принимать следующие параметры:
# # none: переносы отстуствуют, но можно сделать горизонтальную прокрутку
# # char: переносы осуществляются по символам
# # word: переносы осуществляются по словам

# char_editor = Text(height=5, wrap="char")
# char_editor.pack(anchor=N, fill=X)
 
# word_editor = Text(height=5, wrap="word")
# word_editor.pack(anchor=S, fill=X)

###############################################################################################

# Прокрутка текста
# Используя Scrollbar, можно добавить в Text прокрутку текста:

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
 
editor = Text(wrap = "none")
editor.grid(column = 0, row = 0, sticky = NSEW)
 
ys = ttk.Scrollbar(orient = "vertical", command = editor.yview)
ys.grid(column = 1, row = 0, sticky = NS)
xs = ttk.Scrollbar(orient = "horizontal", command = editor.xview)
xs.grid(column = 0, row = 1, sticky = EW)
 
editor["yscrollcommand"] = ys.set
editor["xscrollcommand"] = xs.set


###############################################################################################
root.mainloop()

