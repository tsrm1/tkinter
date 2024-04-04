from tkinter import *


root = Tk()                         # Инициалиция окна

root.title("Main window")           # название окна

# установка иконки для окна
# v1. Из файла иконок *.ico
# root.iconbitmap(default="ico/favicon.ico")  
# V2. Из других графических форматов *.png
icon = PhotoImage(file = "ico/icon2.png")
root.iconphoto(False, icon)


# Размеры и начальная позиция окна
# root.geometry("300x250") # окно с шириной в 300 px и высотой 250 px
root.geometry("300x250+400+200")    # "Ширина x Высота + Смещение по X + Смещение по Y"


# получения данных о размере и позиции окна в формате "WidthxHeight+X+Y" 
root.update_idletasks()     
print(root.geometry())      # "300x250+400+200"

# изменение размеров окна
# по умолчанию, размеры окна можно изменять по ширине и высоте, т.е. root.resizable(True, True)
# root.resizable(False, False)
# root.resizable(True, False)
# root.resizable(False, True)

# можно установить минимальные и максимальные размеры окна
root.minsize(200,150)   # минимальные размеры: ширина - 200, высота - 150
# root.maxsize(400,300)   # максимальные размеры: ширина - 400, высота - 300


# Перехват закрытия окна
def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("App was manually closed!")
root.protocol("WM_DELETE_WINDOW", finish)

# # Атрибуты окна
# # Здесь атрибуту fullscreen передается значение True, 
# # благодаря чему устанавливается полноэкранный режим.
# root.attributes("-fullscreen", True)
# # установка прозрачности с помощью атрибута alpha:
# # Значение 0.5 указывает на полупрозрачность
# root.attributes("-alpha", 0.5)
# #  отключение верхней панели окна (за исключением заголовка и крестика для закрытия)
root.attributes("-toolwindow", True)
print(root.attributes())      # - получить список возможных атримутов и их значение
# # ('-alpha', 1.0,             - прозрачность
# #  '-transparentcolor', '',   - цвет порзрачности
# #  '-disabled', 0,            
# #  '-fullscreen', 0,          - запустить в полноэкранном режиме
# #  '-toolwindow', 0,          - скрытие иконки, кнопок свернуть и на весь экран
# #  '-topmost', 0)


root.mainloop()             # Для отображения окна и взаимодействия с пользователем