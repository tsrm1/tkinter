# Button: кнопка
# Label: текстовая метка
# Entry: однострочное текстовое поле
# Text: многострочное текстовое поле
# Checkbutton: флажок
# Radiobutton: переключатель или радиокнопка
# Frame: фрейм, который организует виджеты в группы
# Listbox: список
# Combobox: выпадающий список
# Menu: элемент меню
# Scrollbar: полоса прокрутки
# Treeview: позволяет создавать древовидные и табличные элементы
# Scale: текстовая метка
# Spinbox: список значений со стрелками для перемещения по элементам
# Progressbar: текстовая метка
# Canvas: текстовая метка
# Notebook: панель вкладок


from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# создаем кнопку из пакета tkinter
btn1 = Button(text="Click")                  # создаем кнопку из пакета tkinter
btn1.pack()                                  # размещаем кнопку в окне
# создаем кнопку из пакета ttk
# v1
btn2 = ttk.Button(text="Click")              # создаем кнопку из пакета ttk
btn2.pack()                                  # размещаем кнопку в окне
# v2
btn = ttk.Button()
btn.pack()
# устанавливаем параметр text
btn["text"]="Send"                          # устанавливаем название кнопки
# получаем значение параметра text
btnText = btn["text"]
print(btnText)
# v3
btn3 = ttk.Button()
btn3.pack()
# устанавливаем параметр text
btn3.config(text="Send Email")


# # Получение информации о виджете
# Для получения информации о виджете можно использовать ряд его атрибутов. Рассмотрим некоторые из них:
# winfo_class: возвращает класс виджета, например, для кнопки это класс TButton
# winfo_children: возвращает для текущего виджета список вложенных виджетов
# winfo_parent: возвращает родительский виджет
# winfo_toplevel: возвращает окно, которое содержит данный виджет
# winfo_width и winfo_height: текущая ширина и высота виджета
# winfo_reqwidth и winfo_reqheight: запрошенная виджетом ширина и высота
# winfo_x и winfo_y: x и y координаты верхнего левого угла виджета относительно родительского элемента
# winfo_rootx и winfo_rooty: x и y координаты верхнего левого угла виджета относительно экрана
# winfo_viewable: указывает, отображается ли виджет или скрыт
# уровень в визуальной иерархии элементов (depth)

def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    print("   "*depth + f"{widget_class} width={widget_width} height={widget_height}  x={widget_x} y={widget_y}")
    for child in widget.winfo_children():
        print_info(child, depth+1)


# Чтобы установленные размеры и позиции были применены к виджетам до вызыва root.mainloop(), 
# вызываем метод root.update()
root.update()     # обновляем информацию о виджетах
 
print_info(root)
# print_info(root, -1)

# Tk width=300 height=250  x=400 y=200
#    Button width=37 height=26  x=131 y=0
#    TButton width=76 height=25  x=112 y=26
#    TButton width=76 height=25  x=112 y=51
#    TButton width=76 height=25  x=112 y=76

print_info(btn3)

# TButton width=76 height=25  x=112 y=76

# получение досутпных параметров виджета
print(btn3.__dict__)


# удаление виджетов
# widget_name.destroy()





root.mainloop()                             # Для отображения окна и взаимодействия с пользователем
