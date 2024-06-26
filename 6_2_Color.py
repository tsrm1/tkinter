from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################
# The symbolic names recognized by Tk and their 8-bit-per-channel RGB values are:
# https://tcl.tk/man/tcl8.6/TkCmd/colors.htm


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

# Установка цвета
# у виджета Label можно установить параметры foreground и background, 
# которые отвечают за цвет текста и фона соответственно. 
# У некоторых виджетов настройки цвета спрятаны в параметре style.

# Именнованные цвета, например, "red", который соответствует красному цвету. 

label = ttk.Label(text="Hello World", 
                    padding=8,
                    foreground="#01579B", 
                    background="#B3E5FC")
label.pack(anchor=CENTER, expand=1)

###############################################################################################

def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb  
 
label = ttk.Label(text="Hello World", 
                    padding=8,
                    foreground=get_rgb((0, 77, 64)), 
                    background=get_rgb((128, 203, 196)))
label.pack(anchor=CENTER, expand=1)


###############################################################################################
root.mainloop()