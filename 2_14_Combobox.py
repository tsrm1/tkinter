from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Combobox
# Виджет Combobox представляет выпадающий список, 
# из которого пользователь может выбрать один элемент. 
# Фактически он представляет комбинацию виджетов Entry и Listbox.

# параметры конструктора Combobox:
# values: список строк для отображения в Combobox
# background: фоновый цвет
# cursor: курсор указателя мыши при наведении на текстовое поле
# foreground: цвет текста
# font: шрифт текста
# justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю
# show: задает маску для вводимых символов
# state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED
# textvariable: устанавливает привязку к элементу StringVar
# height: высота элемента
# width: ширина элемента

languages = ["Python", "C#", "Java", "JavaScript"]
combobox1 = ttk.Combobox(values=languages)
combobox1.pack(anchor=NW, padx=6, pady=6)
###############################################################################################

languages = ["Python", "C#", "Java", "JavaScript"]
# по умолчанию будет выбран первый элемент из languages
languages_var = StringVar(value=languages[2])   
 
label = ttk.Label(textvariable=languages_var)
label.pack(anchor=NW, padx=6, pady=6)
 
combobox2 = ttk.Combobox(textvariable=languages_var, values=languages)
combobox2.pack(anchor=NW, padx=6, pady=6)
 
print(combobox2.get())
###############################################################################################

# По умолчанию мы можем ввести в текстовое поле в Combobox любое значение, 
# даже то, которого нет в списке. Такое поведение не всегда может быть удобно. 
# В этом случае мы можем установить для виджета состояние только для чтения, 
# передав параметру "state" значение "readonly":
combobox3 = ttk.Combobox(textvariable=languages_var, values=languages, state="readonly")
combobox3.pack(anchor=NW, padx=6, pady=6)

# Выбранный элемент можно получить с помощью метода get() класса Combobox
selection = combobox3.get()
# либо с помощью метода get() привязанной переменной
selection = languages_var.get()

# Для установки нового значения можно использовать метод set():
new_value = 'new_value'
languages_var.set(new_value)
combobox3.set(new_value)

# Для установки по индексу из привязанного набора значений также можно использовать 
# метод current(newindex), где с помощью параметра newindex задается 
# индекс выбранного значения. 
# Например, выберем второй элемент:
combobox3.current(1)
###############################################################################################


def selected(event):
    # получаем выделенный элемент
    selection = combobox.get()
    print(selection)
    label["text"] = f"вы выбрали: {selection}"
 
languages = ["Python", "C#", "Java", "JavaScript"]
label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)
 
combobox = ttk.Combobox(values=languages, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)



###############################################################################################
root.mainloop()
