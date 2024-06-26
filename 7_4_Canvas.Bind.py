from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("700x700+100+100")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# С помощью метода tag_bind() можно привязать к определенному элементу в Canvas (например, к линии) событие:
# tag_bind(тег_или_идентификатор_элемента, событие, функция)
# Первый параметр представляет тег или идентификатор элеиментов, для которых добавляется событие.
# Второй параметр - обрабатываемое событие.
# Третий параметр - функция, которая выполняется при возникновении события

canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(fill=BOTH, expand=1)
 
# размеры прямоугольника
big_size = (60, 60, 150, 150)
small_size = (60, 60, 100, 100)
 
# обработчики событий
def make_big(event): canvas.coords(id, big_size)
def make_small(event): canvas.coords(id, small_size)
 
id = canvas.create_rectangle(small_size, fill="red")
# привязка событий к элементу с идентификатором id
canvas.tag_bind(id, "<Enter>", make_big)    # "<Enter>"-событие вхождения курсора в пределы прямогольника
canvas.tag_bind(id, "<Leave>", make_small)  # "<Leave>"-событие выхода указателя мыши за пределы прямоугольника


###############################################################################################
root.mainloop()