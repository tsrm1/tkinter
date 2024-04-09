from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Режим и обработка выбора
# По умолчанию Listbox позволяет выбрать один элемент. Но с помощью параметра selectmode это поведение можно переопределить. Данный параметр принимает одно из следующих значений:
# BROWSE: позволяет выбирать один элемент и перетаскивать его мышкой. Режим по умолчанию.
# EXTENDED: позволяет выбрать группу элементов, выделив начальный и конечный элементы
# SINGLE: позволяет выбрать один элемент, но не позволяет перетаскивать его мышкой
# MULTIPLE: позволяет выбрать множество элементов, надимая на строку элемента.

# Для обработки выбора элементов в Listbox необходимо прикрепить функцию обработки 
# к событию <<ListboxSelect>> с помощью метода bind:

# Функция должна принимать один параметр, который несет информацию о событии 
# - здесь это параметр event, не используется
def selected(event):
    # получаем индексы выделенных элементов
    selected_indices = languages_listbox.curselection()
    print(selected_indices)
    # получаем сами выделенные элементы
    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indices])
    msg = f"вы выбрали: {selected_langs}"
    selection_label["text"] = msg
 
languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)
 
selection_label = ttk.Label()
selection_label.pack(anchor=NW, fill=X, padx=5, pady=5)
 
languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
languages_listbox.bind("<<ListboxSelect>>", selected)


# Программное выделение
# Ряд методов Listbox позволяют программно управлять выделением элементов:
# select_set(first, last): выделяет с индекса first по индекс last. 
# Если надо выделить только один элемент, то применяется только параметр first
# select_includes(index): возвращает True, среди элемент с индексом index выделен
# select_clear(first, last): снимает выделение с индекса first по индекс last. 
# Если надо снять выделение только с одного элемента, 
# то применяется только параметр first
languages_listbox.select_set(first=1, last=2)


###############################################################################################
root.mainloop()
