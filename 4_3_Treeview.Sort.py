from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("600x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# С помощью параметра command метода heading() можно привязать к заголовку некоторую функцию, которая будет вызываться по нажатию на заголовок.
# treeview.heading(имя_заголовка, command=функция)



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


def sort(col, reverse):
    # получаем все значения столбцов в виде отдельного списка
    l = [(tree.set(k, col), k) for k in tree.get_children("")]
    # сортируем список
    l.sort(reverse=reverse)
    # переупорядочиваем значения в отсортированном порядке
    for index,  (_, k) in enumerate(l):
        tree.move(k, "", index)
    # в следующий раз выполняем сортировку в обратном порядке
    tree.heading(col, command=lambda: sort(col, not reverse))


# предполагается, что в папке приложения располагается файл email_icon_micro.png
email_icon = PhotoImage(file="./ico/email_mini.png")

# определяем заголовки
tree.heading("name", text="Имя", anchor=W, command=lambda: sort(0, False))
tree.heading("age", text="Возраст", anchor=W, command=lambda: sort(1, False))
tree.heading("email", text="Email", anchor=W, command=lambda: sort(2, False), image=email_icon)


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