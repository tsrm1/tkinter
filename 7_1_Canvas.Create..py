from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("700x700+100+100")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Canvas
# Добавление элементов на Canvas
# Виджет Canvas предоставляет возможности рисования двухмерных фигур. Стоит отметить, 
# что Canvas есть только в пакете tkinter, а в пакете tkinter.ttk аналог отсутствует.
# Некоторые основные параметры Canvas:
# bg / background: фоновый цвет
# bd / border: граница
# borderwidth: толщина границы
# cursor: курсор
# height: высота виджета
# width: ширина виджета
canvas = Canvas(bg="white", width=650, height=650)
canvas.pack(anchor=CENTER, expand=1)
    
###############################################################################################

# Для двухмерного рисования Canvas предоставляет ряд методов:

# create_line(): рисует линию
# create_rectangle(): рисует прямоугольник
# create_oval(): рисует овал
# create_arc(): рисует дугу
# create_polygon(): рисует многоугольник
# create_text(): добавляет текст
# create_image(): добавляет изображение
# create_window(): добавляет виджет

# В качестве результата все эти методы возвращают идентифтикатор добавленного элемента. 
# Этот идентификатор в дальнейшем может использоваться для управления элементом.

###############################################################################################
# Создание линии
# Для рисования линии применяется метод create_line(). 
# create_line(__x0: float, __y0: float, __x1: float, __y1: float)
# x0 и y0  координаты начальной точки линии, а 
# x1 и y1 - конечной.
canvas.create_line(10, 10, 200, 50)

###############################################################################################
# Параметры отрисовки
# у данного метода можно выделить ряд дополнительных параметров:
# arrow: помещает стрелку в начале линии (значение first), в конце (last) или на обоих концах (both)
# arrowshape: позволяет изменить форму стрелки
# capstyle: если линия не имеет стрелки, то устанавливает, как завершается линия. Принимает значения: butt (по умолчанию), projecting и round
# joinstyle: управляет соединением сегметов линии. Принимает значения: round (по умолчанию), bevel и miter
# smooth: если значение "true" или "bezier", сглаживает сегменты линии
# splinesteps: управляет сглаживанием изогнутых линий

# Методы отрисовки имеют ряд параметров, которые позволяют настроить стилизацию фигур. Некоторые из этих параметров:
# fill: цвет заполнения фигуры
# width: ширина линий
# outline: для заполненных фигур цвет контура
# dash: устанавливает пунктирную линию
# stipple: устанавливает шаблон для заполнения фигуры (например, gray75, gray50, gray25, gray12)
# activefill: цвет заполнения фигуры при наведении курсора
# activewidth: ширина линий при наведении курсора
# activestipple: шаблон заполнения фигуры при наведении курсора
canvas.create_line(10, 50, 200, 90, activefill="red", fill="blue", dash=2)
canvas.create_line(10, 100, 200, 100, activefill="red", fill="blue", dash=2)

###############################################################################################

# Создание прямоугольника

# Для отрисовки прямоугольника применяется метод create_rectangle(), 
# которому обязательно передаются координаты верхнего левого и правого нижнего угла:
# create_rectangle(x0: float, y0: float, x1: float, y1: float)

canvas.create_rectangle(10, 120, 200, 160, fill="#80CBC4", outline="#004D40")

###############################################################################################

# Отрисовка овала
# Для отрисовки овала применяется метод create_oval(). 
# В качестве обязательных параметров он принимает координаты прямоугольника, 
# в который будет вписан овал. :
# create_oval(x0: float, y0: float, x1: float, y1: float)

canvas.create_oval(10, 180, 200, 250, fill="#80CBC4", outline="#004D40")

###############################################################################################

# Отрисовка многоугольника
# Для создания многоугольника применяется метод create_polygon().

canvas.create_polygon(210, 30, 400, 200, 400, 30, fill="#80CBC4", outline="#004D40")

###############################################################################################

# можно передавать набор кортежей, где каждый кортеж представляет отдельную точку:

points = (
    (410, 30),
    (600, 200),
    (600, 30),
)
canvas.create_polygon(*points, fill="#80CBC4", outline="#004D40")
###############################################################################################

# Отрисовка дуги
# Для отрисовки дуги применяется метод create_arc()

canvas.create_arc((200, 200), (300, 300), fill="#80CBC4", outline="#004D40")
canvas.create_arc((200, 200), (350, 300), fill='red', outline="#004D40")

###############################################################################################

# Отображение текста
# Для вывода текста применяется метод create_text(). 
# Ключевыми его параметрами являются координаты точки вывода текста, 
# а также параметр text - сам выводимый текст:

canvas.create_text(50, 50, text="Hello WORLD", fill="#004D40")
 
canvas.create_text(50, 100, anchor=NW, text="Hello WORLD", fill="red")
# во втором случае установлен параметр anchor: его значение "NW" указывает, 
# что координаты будут представлять верхний левый угол прямогольной области, 
# в которой выводится текст

# С помощью параметра font можно задать шрифт, в том числе его высоту:
canvas.create_text(50, 150, font="Arial 14", anchor=NW, text="Hello WORLD", fill="blue")

###############################################################################################

# Вывод изображения
# Для вывода изображения применяется метод create_image(), 
# который в качестве обязательно параметра принимает координаты изображения. 
# Для установки самого изображения в метод через параметр image передается ссылка на изображение:

python_image = PhotoImage(file="./ico/icon2.png")
 
canvas.create_image(450, 450, anchor=NW, image=python_image)

# по умолчанию координаты представляют центр изображения
# anchor=NW  -  координата представляет верхний левый угол изображения.
###############################################################################################

# Добавление виджетов
# Одной из замечательных особенностей Canvas является то, 
# что он позволяет добавлять другие виджеты и 
# таким образом создавать сложные по композиции интерфейсы. 
# Для этого применяется метод create_window().
# create_window(__x: float, __y: float, *, anchor: _Anchor = ..., height: _ScreenUnits = ..., state: Literal['normal', 'active', 'disabled'] = ..., tags: str | list[str] | tuple[str, ...] = ..., width: _ScreenUnits = ..., window: Widget = ...) -> _CanvasItemId
# create_window(__coords: tuple[float, float] | list[int] | list[float], *, anchor: _Anchor = ..., height: _ScreenUnits = ..., state: Literal['normal', 'active', 'disabled'] = ..., tags: str | list[str] | tuple[str, ...] = ..., width: _ScreenUnits = ..., window: Widget = ...) -> _CanvasItemId

# Параметры
# _x и _y или __coords: координаты точки размещения виджета. По умолчанию представляет центр виджета
# _anchor: устанавливает положение виджета относительно координат
# height: высота виджета
# width: ширина виджета
# state: состояние виджета
# tags: набор тегов, связанных с виджетом

btn = ttk.Button(text="Click")
canvas.create_window(300, 300, anchor=NW, window=btn, width=100, height=50)
###############################################################################################

# Создание прокрутки
# Для создания прокрутки виджет Canvas предоставляет параметр, 
# который позволяет установить прокручиваемую область:
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
h = ttk.Scrollbar(orient=HORIZONTAL)
v = ttk.Scrollbar(orient=VERTICAL)
canvas = Canvas(scrollregion=(0, 0, 1000, 1000), bg="white", yscrollcommand=v.set, xscrollcommand=h.set)
h["command"] = canvas.xview
v["command"] = canvas.yview
 
canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
 
canvas.create_rectangle(10,10, 300, 300, fill="red")

###############################################################################################
root.mainloop()