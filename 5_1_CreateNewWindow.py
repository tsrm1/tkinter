from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# # Создание окон
# # октроем новое окно по нажатию на кнопку:
# def click():
#     window = Tk()
#     window.title("Новое окно")
#     window.geometry("250x200")
#     close_button = ttk.Button(window, text="Закрыть окно", command=lambda: window.destroy())
#     close_button.pack(anchor="center", expand=1)
 
# button = ttk.Button(text="Создать окно", command=click)
# button.pack(anchor=CENTER, expand=1)


# # Удаление окна
# # Для удаления окна применяется метод destroy()

###############################################################################################


# # Определение окна в объектно-ориентированном стиле
# # В примере выше новое окно, его параметры и вложенные виджеты определялись внутри функции, 
# # однако это приводит к разбуханию кода функции. И гораздо проще вынести определение окна в отдельный класс:

# class Window(Tk):
#     def __init__(self):
#         super().__init__()
 
#         # конфигурация окна
#         self.title("Новое окно")
#         self.geometry("250x200")
 
#         # определение кнопки
#         self.button = ttk.Button(self, text="закрыть")
#         self.button["command"] = self.button_clicked
#         self.button.pack(anchor="center", expand=1)
 
#     def button_clicked(self):
#         self.destroy()
 
 
# def click():
#     window = Window()
 
# open_button = ttk.Button(text="Создать окно", command=click)
# open_button.pack(anchor="center", expand=1)

###############################################################################################

# # Окно поверх других окон
# # Для создания диалогового окна, которое располагается поверх главного окна, применяется класс Toplevel:

# def dismiss(window):
#     window.grab_release() 
#     window.destroy()
 
# def click():
#     window = Toplevel()
#     window.title("Новое окно")
#     window.geometry("250x200")
#     window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window)) # перехватываем нажатие на крестик
#     close_button = ttk.Button(window, text="Закрыть окно", command=lambda: dismiss(window))
#     close_button.pack(anchor="center", expand=1)
#     window.grab_set()       # захватываем пользовательский ввод
 
# open_button = ttk.Button(text="Создать окно", command=click)
# open_button.pack(anchor="center", expand=1)


# # Toplevel по сути то же самое окно Tk, которое располагается поверх других окон. В примере выше оно также имеет кнопку. Но кроме того, чтобы пользователь не мог перейти обратно к главному окну пока не закроет это диалоговое окно, применяется ряд методов. Прежде всего захватываем весь пользовательский ввод с помощью метода grab_set():
# # window.grab_set()
# # В функции dismiss(), которая закрывает окно, освобождаем ввод с помощью метода grab_release()
# # window.grab_release()

###############################################################################################

result = StringVar()

def create_window():
    window = Toplevel()
    # window = Tk()
    window.title("Some title")
    window.geometry("300x300")

    ttk.Entry(window, textvariable=result).pack()
    ttk.Button(window, text="create window", command=show_var).pack()
    ttk.Label(window, textvariable=result).pack()

def show_var():
    print(result.get()) 

ttk.Button(text="click me", command=create_window).pack()


###############################################################################################
root.mainloop()