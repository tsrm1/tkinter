from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("700x700+100+100")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Установка тегов
# Для установки тега элементу при его добавлении можно использовать параметр tags, 
# который получает список тегов:
# canvas.create_line(10, 10, 200, 100, fill="red", tags=["line"])

# Добавление тега
# Для добавления тега можно использовать метод addtag():
# addtag(название_тега, команда, идентификатор_элемента)

# Первый параметр - добавляемый тег, второй параметр - команда, обычно "withtag". Третий параметр - идентификатор элемента, для которого добавляется тег:
# line_id = canvas.create_line(10, 10, 200, 100, fill="red", tags=["line"])
# canvas.addtag("figure", "withtag", line_id)

###############################################################################################
# Получение тегов
# Для получения списка тегов для определенного элемента применяется метод gettags(), в который передается идентификатор элеимента:

# line_id = canvas.create_line(10, 10, 200, 100, fill="red", tags=["line", "figure"])
# # получаем все теги для элемента line_id
# for tag in canvas.gettags(line_id):
#     print(tag)


###############################################################################################
# можно получить идентификаторы элементов по определенному тегу с помощью метода find_withtag(), в который передается имя тега.

# canvas.create_line(10, 10, 200, 10, fill="red", tags=["line", "figure"])
# canvas.create_line(10, 50, 200, 50, fill="blue", tags="line")
# # получаем все элементы с тегом line
# for element_id in canvas.find_withtag("line"):
#     print(element_id)


###############################################################################################
# Удаление тега
# Для удаления тега применяется метод dtags()

# line_id = canvas.create_line(10, 10, 200, 10, fill="red", tags=["line", "figure"])
# # удаляем у элемента line_id тег "figure"
# canvas.dtag(line_id, "figure")

###############################################################################################
# Конфигурация через тег
# С помощью метода itemconfigure() для элементов с определенным тегом можно установить различные опции

# itemconfigure: (tagOrId: str | _CanvasItemId, cnf: dict[str, Any] | None = ..., **kw: Any)
# Первый параметр - тег или идентификатор элемента, а второй - набор устанавливаемых опций. Например:

# canvas.create_line(10, 50, 200, 50, fill="blue", tags="line")
# # устанавливаем для элементов с тегом "line" зеленый цвет
# canvas.itemconfigure("line", fill="green")

###############################################################################################

# Практическое использование тегов
# позволяют управлять группой элементов:

red = "red"
blue= "blue"
green = "green"
selected_color = StringVar(value=red)
 
canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(anchor=NW)
 
canvas.create_rectangle((10, 80, 130, 130), fill=selected_color.get(), outline="black", tags="house")
canvas.create_polygon((10, 80), (70, 30), (130, 80), fill=selected_color.get(), outline="black", tags="house")
 
def select():
    canvas.itemconfigure("house", fill=selected_color.get())
 
ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6).pack(anchor=NW)
ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6).pack(anchor=NW)
ttk.Radiobutton(text=green, value=green, variable=selected_color, command=select, padding=6).pack(anchor=NW)
 


###############################################################################################
root.mainloop()