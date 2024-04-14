from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# # Выделение строк таблицы
# # Для работы с выделенными строками в Treeview определен ряд методов:
# # selection(): возвращает идентификаторы выделенных строк в виде кортежа
# # selection_add(items): выделяет строки с идентификаторами, которые передаются в качестве параметра
# # selection_remove(items): снимает выделение строк с идентификаторами, которые передаются в качестве параметра
# # selection_set(items): снимает выделение с ранее выделенных строк и выделяет строки с идентификаторами, 
# # которые передаются в качестве параметра

# # Обработка события выделения
# # Для обработки выделения строк у Treeview применяется событие <<TreeviewSelect>>

# root.rowconfigure(index=0, weight=1)
# root.columnconfigure(index=0, weight=1)
 
# # определяем данные для отображения
# people = [
#     ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
#     ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
#     ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
#     ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
#     ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
#     ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
#     ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
#     ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
#     ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
#     ]
 
# # определяем столбцы
# columns = ("name", "age", "email")
 
# tree = ttk.Treeview(columns=columns, show="headings")
# tree.grid(row=0, column=0, sticky="nsew")


# def sort(col, reverse):
#     # получаем все значения столбцов в виде отдельного списка
#     l = [(tree.set(k, col), k) for k in tree.get_children("")]
#     # сортируем список
#     l.sort(reverse=reverse)
#     # переупорядочиваем значения в отсортированном порядке
#     for index,  (_, k) in enumerate(l):
#         tree.move(k, "", index)
#     # в следующий раз выполняем сортировку в обратном порядке
#     tree.heading(col, command=lambda: sort(col, not reverse))


# # предполагается, что в папке приложения располагается файл email_icon_micro.png
# email_icon = PhotoImage(file="./ico/email_mini.png")

# # определяем заголовки
# tree.heading("name", text="Имя", anchor=W, command=lambda: sort(0, False))
# tree.heading("age", text="Возраст", anchor=W, command=lambda: sort(1, False))
# tree.heading("email", text="Email", anchor=W, command=lambda: sort(2, False), image=email_icon)


# tree.column("#1", stretch=NO, width=100)
# tree.column("#2", stretch=NO, width=70)
# tree.column("#3", stretch=NO, width=120)
 
# # добавляем данные
# for person in people:
#     tree.insert("", END, values=person)
 
# # добавляем вертикальную прокрутку
# scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky="ns")

###############################################################################################


# определяем данные для отображения
people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
 
label = ttk.Label()
label.pack(anchor=N, fill=X)
# определяем столбцы
columns = ("name", "age", "email")
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(expand=1, fill=BOTH)
 
# определяем заголовки
tree.heading("name", text="Имя", anchor=W)
tree.heading("age", text="Возраст", anchor=W)
tree.heading("email", text="Email", anchor=W)
 
tree.column("#1", stretch=NO, width=70)
tree.column("#2", stretch=NO, width=60)
tree.column("#3", stretch=NO, width=100)
 
# добавляем данные
for person in people:
    tree.insert("", END, values=person)
 
def item_selected(event):
    selected_people = ""
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        person = item["values"]
        selected_people = f"{selected_people}{person}\n"
    label["text"]=selected_people
 
tree.bind("<<TreeviewSelect>>", item_selected)


# Режим выделения
# По умолчанию в Treeview можно выделить только один элемент (одну строку). За установку режима выделения в Treeview отвечает параметр selectionmode, который может принимать следующие значения:
# extended: позволяет выбрать несколько строк
# browse: позволяет выбрать только одну строку
# none: выделение строк не доступно
# Например, изменим код Treeview, установив режим "extended":
# tree = ttk.Treeview(columns=columns, show="headings", selectmode="extended")


###############################################################################################
root.mainloop()