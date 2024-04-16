from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("700x700+100+100")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# # Управление координатами
# # Для получения/изменения координат элеимента применяется метод coords():
# # получение координат
# coords(__tagOrId: str | _CanvasItemId, /) -> list[float]     
# - возвращает координаты в виде списка значений для элемента с определенным идентификатором.

# # изменение координат
# coords(__tagOrId: str | _CanvasItemId, __args: list[int] | list[float] | tuple[float, ...], /) -> None
# coords(__tagOrId: str | _CanvasItemId, __x1: float, __y1: float, *args: float) -> None
# - изменяют позицию, получая в качестве второго/третьего параметра(ов) новые координаты.


y = 0
direction = -10
btn_height = 40
canvas_height = 200
 
canvas = Canvas(bg="white", width=250, height=canvas_height)
canvas.pack(anchor=CENTER, expand=1)
 
def cliked_button():
    global y, direction
    if y >= canvas_height - btn_height or y <=0: direction = direction * -1
    y = y + direction
    canvas.coords(btnId, 10, y)
 
btn = ttk.Button(text="Click", command=cliked_button)
btnId = canvas.create_window(10, y, anchor=NW, window=btn, width=100, height=btn_height)


###############################################################################################
root.mainloop()