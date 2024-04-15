from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# # Окна сообщений
# # Tkinter имеет ряд встроенных окон для разных ситуаций, в частности, окна сообщений, функционал которых заключен в модуле tkinter.messagebox. Для отображения сообщений этот модуль предоставляет следующие функции:
# # showinfo(): предназначена для отображения некоторой информации
# # showerror(): предназначена для отображения ошибок
# # showwarrning(): предназначена для отображения предупреждений

# # Все эти функции принимают три параметра:
# # showinfo(title, message, **options)
# # showerror(title, message, **options)
# # showwarrning(title, message, **options)
# # title: заголовок окна
# # message: отображаемое сообщение
# # options: настройки окна
# from tkinter.messagebox import showerror, showwarning, showinfo

# def open_info(): 
#     showinfo(title="Информация", message="Информационное сообщение")
 
# def open_warning(): 
#     showwarning(title="Предупреждение", message="Сообщение о предупреждении")
 
# def open_error(): 
#     showerror(title="Ошибка", message="Сообщение об ошибке")
 
# info_button = ttk.Button(text="Информация", command=open_info)
# info_button.pack(anchor="center", expand=1)
 
# warning_button = ttk.Button(text="Предупреждение", command=open_warning)
# warning_button.pack(anchor="center", expand=1)
 
# error_button = ttk.Button(text="Ошибка", command=open_error)
# error_button.pack(anchor="center", expand=1)

###############################################################################################

from tkinter.messagebox import showinfo, askyesnocancel

def click(): 
    result =  askyesnocancel(title="Подтвержение операции", message="Подтвердить операцию?")
    if result==None: showinfo("Результат", "Операция приостановлена")
    elif result: showinfo("Результат", "Операция подтверждена")
    else : showinfo("Результат", "Операция отменена")
 
ttk.Button(text="Click", command=click).pack(anchor="center", expand=1)

###############################################################################################

# # Настройка окон
# # Дополнительно все вышерассмотренные функции принимают ряд параметров, 
# # которые могут применяться для настройки окон. Некоторые из них:

# # detail: дополнительный текст, который отображается под основным сообщением

# # icon: иконка, которая отображается рядом с сообщением. Должна представлять одно из втроенных изображений: 
# # info, error, question или warning

# # default: кнопка по умолчанию. Должна представлять одно из встроенных значений: 
# # abort, retry, ignore, ok, cancel, no, yes

# from tkinter.messagebox import OK, INFO, showinfo 

# def click(): 
#     showinfo(title="METANIT.COM", message="Добро пожаловать", 
#             detail="Hello World!", icon=INFO, default=OK)
 
# ttk.Button(text="Click", command=click).pack(anchor="center", expand=1)

###############################################################################################
root.mainloop()