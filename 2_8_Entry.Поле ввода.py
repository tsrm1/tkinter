from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x350+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# Поле ввода Entry:

# ряд параметров
# background: фоновый цвет
# cursor: курсор указателя мыши при наведении на текстовое поле
# foreground: цвет текста
# font: шрифт текста
# justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, 
# CENTER - по центру, RIGHT - по правому краю
# show: задает маску для вводимых символов
# state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED
# textvariable: устанавливает привязку к элементу StringVar
# width: ширина элемента

# ряд методов:
# insert(index, str): вставляет в текстовое поле строку по определенному индексу
# get(): возвращает введенный в текстовое поле текст
# delete(first, last=None): удаляет символ по индексу first. 
# Если указан параметр last, то удаление производится до индекса last. 
# Чтобы удалить до конца, в качестве второго параметра можно использовать значение END.
# focus(): установить фокус на текстовое поле



# # Простейшее текстовое поле:
# ttk.Entry().pack(anchor=NW, padx=8, pady= 8)




# Вставка и удаление текста
text_start = "Enter text here"
def clear():
    entry.delete(0, END)                # удаление введенного текста
    entry.insert(0, text_start)         # вставка текста по умолчанию

def display():
    if entry.get() != text_start:
        label["text"] = entry.get()     # получаем введенный текст
        clear()

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)


# entry.insert(0, "Hello World")        # вставка начальных данных
entry.insert(0, text_start)             # вставка начальных данных

btn = ttk.Button(text="Click", command=display) # Выводим кнопку и отслеживаем её нажатие
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)




# Валидация
# С помощью параметра validate конструктора Entry можно задать, 
# когда проводить валидацию введенного значения. 
# значения параметрa:
# none: отсутствие валидации, значение по умолчанию
# focus: валидация при получении фокуса
# focusin: валидация при изменении фокуса
# focusout: валидация при потере фокуса
# key: валидация при каждом вводе нового символа
# all: валидация при измении фокуса и вводе символов в поле

# пользовтаель должен ввести номер телефона в формете +xxxxxxxxxxx. 
# То есть сначала должен идти знак +, а затем 11 цифр, например, +12345678901:
import re

def is_valid(newval):
    return re.match("^\+\d{0,11}$", newval) is not None
# Она принимает один параметр - текущее значение Entry, которое надо валидировать. 
# Она возвращает True, если значение прошло валидацию, и False, если не прошло. 
# Сама логика валидации представляет проверку строки на регулярное выражение "^\+\d*$". 
# Если новое значение соответствует этому выражению, и в нем не больше 12 символов, 
# то оно прошло валидацию.
# В итоге мы сможем ввести в текстовое поле только символ + и затем только 11 цифр.

check = (root.register(is_valid), "%P")
# Первый элемент - вызов метода root.register(is_valid) регистрирует функцию, 
# которая собственно будет производить валидацию - это функция is_valid(). 
# Второй элемент - подстановка "%P" представляет новое значение, 
# которое передается в функцию валидации

# параметр validate="key" указывает, 
# что мы будем валидировать ввод при каждом нажати на клавиатуру
phone_entry = ttk.Entry(validate="key", validatecommand=check) 
phone_entry.pack(padx=5, pady=50, anchor=NW)

###############################################################################################
root.mainloop()
