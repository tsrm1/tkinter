from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Виджет Scrollbar прокручивать содержимое контейнера, которое больше размеров этого контейнера.
# Основные параметры конструктора Scrollbar:
# orient: направление прокрутки. 
# Может принать следующие значения: 
# vertical (вертикальная прокрутка) и 
# horizontal (горизонтальная прокрутка).
# command: команда прокрутки
# Scrollbar не используется сам по себе, он применяется лишь для прокручиваемого виджета. 
# Не все виджеты в tkinter являются прокручиваемыми. 
# Для прокрутки по вертикали прокручиваемый виджет имеет yview, 
# а для прокрутки по горизонтали - метод xview 
# (виджет может иметь только один из этих методов). 
# Примером прокручиваемого виджета может служить Listbox или Text. 
# Этот метод используется в качестве команды для Scrollbar:

# listbox = Listbox()
# # вертикальная прокрутка
# scrollbar = ttk.Scrollbar(orient="vertical", command = listbox.yview)
# # горизонтальная прокрутка
# scrollbar = ttk.Scrollbar(orient="horizontal", command = listbox.xview)


# Ручная прокрутка
# Для прокрутки виджет может содержать специальные методы:
# yview_scroll(number, what): сдвигает текущее положение по вертикали. Параметр number указывает количество, на которое надо сдвигать. А параметр what определяет единицы сдвига и может принимать следующие значения: "units" (элемент) и "pages" (страницы)
# xview_scroll(number, what): сдвигает текущее положение по горизонтали
# yview_moveto(fraction): сдвигает область просмотра по вертикали на определенную часть, которая выражается во float от 0 до 1
# xview_moveto(fraction): сдвигает область просмотра на определенную часть по горизонтали
# сдвигаем скрол на 1 элемент внизу
# listbox.yview_scroll(number=1, what="units")


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

root.columnconfigure(index=0, weight=40)
root.columnconfigure(index=1, weight=10)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)
 
# базовый список
languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C", 
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]
languages_var = StringVar(value=languages)
 
# текстовое поле и кнопка для добавления в список
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, columnspan=2, row=0, padx=5, pady=5)
 
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
languages_listbox.select_set(first=2, last=4)

# вертикальная прокрутка
scrollbar = ttk.Scrollbar(orient="vertical", command=languages_listbox.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.grid(column=2, row=1, padx=0, pady=5, sticky=NSEW)
  
languages_listbox["yscrollcommand"]=scrollbar.set


# Ручная прокрутка
# сдвигаем скрол на 2 элементa вниз
languages_listbox.yview_scroll(number=2, what="units")

ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, columnspan=2, padx=5, pady=5)

###############################################################################################


# languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
#              "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go",
#              "T-SQL", "PL-SQL", "Typescript"]

# languages_var = StringVar(value=languages)
# listbox = Listbox(listvariable=languages_var)
# listbox.pack(side=LEFT, fill=BOTH, expand=1)
  
# scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
  
# listbox["yscrollcommand"]=scrollbar.set


###############################################################################################
root.mainloop()
