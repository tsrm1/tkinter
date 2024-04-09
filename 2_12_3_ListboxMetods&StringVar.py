from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# добавление нового элемента
def add():
    new_language = language_entry.get()
    # добавляем новый элемент в список languages
    languages.append(new_language)
    # переустанавливаем значение переменной languages_var
    languages_var.set(languages)
    print(languages)
 
 # удаление выделенного элемента
def delete():
    selection = languages_listbox.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    languages.pop(selection[0])
    languages_var.set(languages)
    print(languages)

root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)
 
# базовый список
languages = ["Python", "C#"]
languages_var = StringVar(value=languages)
 
# текстовое поле и кнопка для добавления в список
language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
 
# создаем список
languages_listbox = Listbox(listvariable=languages_var)
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=5)

ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)

###############################################################################################
root.mainloop()
