from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("700x700+100+100")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Удаление элемента
# Для удаления применяется метод delete(), 
# который в качестве параметра принимает идентификатор удаляемого элемента.

canvas = Canvas(bg="white", width=250, height=200)
canvas.pack(anchor=CENTER, expand=1)
 
 
def remove_button():
    canvas.delete(btnId)
 
btn = ttk.Button(text="Click", command=remove_button)
btnId = canvas.create_window(10, 20, anchor=NW, window=btn, width=100, height=50)


###############################################################################################
root.mainloop()