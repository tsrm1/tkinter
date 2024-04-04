# Основные параметры виджета Button:
# command: функция, которая вызывается при нажатии на кнопку
# compund: устанавливает расположение картинки и текста относительно друг друга
# cursor: курсор указателя мыши при наведении на метку
# image: ссылка на изображение, которое отображается на метке
# pading: отступы от границ вилжета до его текста
# state: состояние кнопки
# text: устанавливает текст метки
# textvariable: устанавливает привязку к элементу StringVar
# underline: указывает на номер символа в тексте кнопки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается
# width: ширина виджета

from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################
 
clicks = 0
 
def click_button():
    global clicks
    clicks += 1
    # изменяем текст на кнопке
    btn["text"] = f"Clicks {clicks}"   

    if clicks > 5:
        btn1["state"]=["enabled"]
 
 
btn = ttk.Button(text="Click Me", command=click_button)

btn1 = ttk.Button(text="Wait", state=["disabled"])




btn.pack()
btn1.pack()
 
root.mainloop()