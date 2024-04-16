from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# Стилизация
# Шрифты

# Имена шрифтов
# Ряд виджетов, например, Label или Text, поддерживают установку шрифта через параметр font. 
# Каждая платформа может определять свои специфические шрифты. 
# Но также библиотека Tk по умолчанию включает ряд именнованных шрифтов, 
# которые могут использоваться на различных компонентах графического интерфейса и 
# которые доступны на всех платформах:

# TkDefaultFont: шрифт по умолчанию, который применяется, 
# если для виджета явным образом не определен шрифт

# TkTextFont: шрифт по умолчанию, 
# который применяется для виджетов Entry, Listbox и ряда других

# TkFixedFont: шрифт с фиксированной шириной

# TkMenuFont: шрифт для пунктов меню

# TkHeadingFont: шрифт для заголовков в Listbox и в таблицах

# TkCaptionFont: шрифт для строки статуса в окнах

# TkSmallCaptionFont: шрифт малого размера для диалоговых окон

# TkIconFont: шрифт для подписей к иконкам

# TkTooltipFont: шрифт для высплывающих окон

# использование шрифтов
# ttk.Label(text="Hello World", font="TkTextFont")

###############################################################################################

# Для их получения списка шрифтов используем функцию names() из пакета tkinter.font:

from tkinter import font
 
for font_name in font.names():
    print(font_name)

# fixed
# oemfixed
# TkDefaultFont
# TkMenuFont
# ansifixed
# systemfixed
# TkHeadingFont
# device
# TkTooltipFont
# defaultgui
# TkTextFont
# ansi
# TkCaptionFont
# system
# TkSmallCaptionFont
# TkFixedFont
# TkIconFont
print("###############################################################################################")
###############################################################################################

from tkinter import font


for family in font.families():
    print(family)

print("###############################################################################################")
###############################################################################################

# Определение шрифта
# За определение шрифта в Tkinter отвечает класс Font из модуля tkinter.font. Он принимет следующие параметры:

# name: имя шрифта

# family: семейство шрифтов

# size: высота шрифта (в точках при положительном значении или в пикселях при негативном значении)

# weight: вес шрифта. Принимает значения normal (обычный) или bold (жирный)

# slant: наклон. Принимает значения roman (обычный) или italic (наклонный)

# underline: подчеркивание. Принимает значения True (с подчеркиванием) или False (без подчеркивания)

# overstrike: зачеркивание. Принимает значения True (с зачеркиванием) или False (без зачеркивания)

# Для получения всех доступных семейств шрифтов на текущей платформе можно использовать функцию families() 
# из модуля tkinter.font

font1 = font.Font(family= "Arial", size=11, weight="normal", slant="roman", underline=True, overstrike=True)
label1 = ttk.Label(text="Hello World", font=font1)
label1.pack(anchor=NW)
 
font2 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
label2 = ttk.Label(text="Hello World", font=font2)

# "Arial 11 normal roman", применяется семейство шрифта Arial, высота 11 единиц, нежирный шрифт без наклона.
label3 = ttk.Label(text="Hello World", font="Arial 11 normal roman")
label3.pack(anchor=NW)
 
label4 = ttk.Label(text="Hello World", font="Verdana 11 normal roman")
label4.pack(anchor=NW)
 


###############################################################################################
root.mainloop()