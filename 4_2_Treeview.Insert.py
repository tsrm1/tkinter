from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Управление данными в Treeview
# Виджет Treeview предназначен для отображения иерархических данных, причем как в виде дерева, так и в виде таблицы. Среди параметров Treeview следует отметить следующие:
# columns: столбцы таблицы в виде строки или списка/кортежа строк
# displaycolumns: отображаемые столбцы таблицы
# cursor: курсор при наведении на виджет
# height: высота виджета
# padding: отступы от границ виджета до содержимого
# selectmode: режим выбора элементов в виджете
# show: формат отображения данных. Может принимать одно из следующих значений:
# tree: отображает столбец #0
# heading: отображает строку с заголовками
# tree headings: отображает столбец #0 и строку с заголовками
# "": не отображает ни столбец #0, ни строку с заголовками

# Управление данными

# Добавление элементов
# Для добавления данных применяется метод insert():
# insert: (parent, index, iid, values) -> str
# метод создает новый элемент и возвращает его идентификатор, который по умолчанию представляет строку наподобие "IOO1". Основные параметры метода:
# parent: представляет идентификатор родительского элемента, в который добавляется элемент. Если создается элемент верхнего уровня, для которого не существует никакого родительского элемента, как, например, в случае с добавлением строки в таблицу, то передается пустая строка.
# index: указывает индекс для вставки элемента. Если элемент добавляется в конец, то используется значение END или "end", либо указывается число, которое равно количеству элементов или больше его. Если элемент добавляется в самое начало, то указывается 0 или число меньше нуля.
# iid: если указан данный параметр, то его значение будет использоваться в качестве идентификатора элемента. При этом подобный в виджете не должно быть элемента с подобным идентификатором, иначе генерируется новый идентификатор, как в обшем случае
# values: список или кортеж значений, которые и составляют добавляемый элемент


# Удаление элементов
# Для удаления данных применяется метод delete():
# delete(items)


# Перемещение элементов
# Для перемещения элемента на другую позицию применяется метод move():
# move(item, parent, index)
# Этот метод создает новый элемент и возвращает его идентификатор, который по умолчанию представляет строку наподобие "IOO1". Основные параметры метода:
# item: идентификатор элемента, который надо переместить.
# parent: представляет родительский элемент перемещаемого элемента .
# index: индекс, на который перемещается элемент


# Получение элементов
# Для получения элементов применяется метод get_children():
# get_children(item)
# Он принимает идентификатор элемента, дочерние элементы которого надо получить, 
# и возвращает набор идентификаторов полученных элементов:
# for k in treeview.get_children(""): print(k)
# В данном случае k представляет идентификатор элемент.

# В качестве параметра в get_children() передается элемент в Treeview, 
# дочерние элементы которого мы хотим получить. Если надо получить элементы верхнего уровня 
# (например, строки таблицы), то передается пустая строка.
# Конкретный элемент по ключу с помощью метода item(), в который передается идентификатор элемента:
# for k in treeview.get_children(""): 
#     print(treeview.item(k))


# Если нам надо получить не весь набор значений, а только одно значение (отдельную ячейку строки), 
# то применяется метод set(), в который передается идентификатор элемента и номер столбца:
# for k in treeview.get_children(""): 
#     print(treeview.set(k, 0))
# В данном случае получаем значение первой ячейки строки (при табличном отображении).


# Изменение значений
# Если надо изменить один столбец, то применяется метод set()
# set(item, column, value)
# item: идентификатор элемента, который надо изменить.
# column: индекс элемента в кортеже (столбца в строке), который надо изменить.
# value: новое значение

# treeview.set("I003", 0, "Admin")
# Здесь значение в первом столбце элемента с id=I003 меняется на строку "Admin"


# Если надо изменить вообще весь элемент со всеми его значениями, то применяется метод item()
# item(item, values)
# item: идентификатор элемента, который надо изменить.
# values: кортеж с новыми значениями
# treeview.item("I003", values=("Tim", 34, "tim@email.com"))
# Здесь элемент с id=I003 в качестве значений принимает кортеж ("Tim", 34, "tim@email.com")



###############################################################################################
# Для отображения данных в виде таблицы параметру show предпочтительно передать значение 
# "headings" (если надо отображать заголовки), либо " " (для таблицы без заголовков).


# Настройка столбца
# с помощью метода heading():
# heading(column, text, image, anchor, command)
# Параметры метода:
# column: имя настраиваемого столбца
# text: текст заголовка
# image: картинка для заголовка
# anchor: устанавливает выравнивание заголовка по определенному краю. Может принимать значения n, e, s, w, ne, nw, se, sw, c
# command: функция, выполняемая при нажатии на заголовок

# Для настройки столбца в целом применяется метод column():
# column(column, width, minwidth, stretch, anchor)
# Параметры метода:
# column: индекс настраиваемого столбца в формате "# номер_столбца"
# width: ширина столбца
# minwidth: минимальная ширина
# anchor: устанавливает выравнивание заголовка по определенному краю. 
# Может принимать значения n, e, s, w, ne, nw, se, sw, c
# stretch: указывает, будет ли столбец растягиваться при растяжении контейнера. 
# Если будет, то значение True, иначе значение False

# При добавлении изображения оно помещается в правой части. 
# Например, установка изображения для третьего столбца:

root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)
 
# определяем данные для отображения
people = [
    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
    ]
 
# определяем столбцы
columns = ("name", "age", "email")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.grid(row=0, column=0, sticky="nsew")
 
# определяем заголовки
tree.heading("name", text="Имя", anchor=W)
tree.heading("age", text="Возраст", anchor=W)
# tree.heading("email", text="Email", anchor=W)

# предполагается, что в папке приложения располагается файл email_icon_micro.png
email_icon = PhotoImage(file="./ico/email_mini.png")
tree.heading("email", text="Email", anchor=W, image=email_icon)

tree.column("#1", stretch=NO, width=100)
tree.column("#2", stretch=NO, width=70)
tree.column("#3", stretch=NO, width=120)
 
# добавляем данные
for person in people:
    tree.insert("", END, values=person)
 
# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")


###############################################################################################
root.mainloop()
