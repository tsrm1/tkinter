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


# добавление нового элемента
def add():
    new_language = language_entry.get()
    # добавляем новый элемент в список languages
    languages.append(new_language)
    print(f'append = {new_language}')
    # переустанавливаем значение переменной languages_var
    languages_var.set(languages)
    print(f'=> {languages}')
 
 # удаление выделенного элемента/списка элементов
def delete():
    selection = languages_listbox.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    del_index = list(selection)
    del_index.sort(reverse=True)
    # print(del_index)
    for i in del_index:
        print(f'delete[{i}] = {languages[i]}')
        languages.pop(i)
    languages_var.set(languages)
    print(f'=> {languages}')

root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)
 
# базовый список
languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = StringVar(value=languages)
 
# текстовое поле и кнопка для добавления в список
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
 
# создаем список
languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
# selectmode=EXTENDED, позволяет выбрать группу элементов, выделив начальный и конечный элементы
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)
# Программное выделение:
# select_set(first, last): выделяет с индекса first по индекс last. 
# Если надо выделить только один элемент, то применяется только параметр first
# select_includes(index): возвращает True, среди элемент с индексом index выделен
# select_clear(first, last): снимает выделение с индекса first по индекс last. 
# Если надо снять выделение только с одного элемента, 
# то применяется только параметр first
languages_listbox.select_set(first=1, last=2)
ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)

###############################################################################################
root.mainloop()
