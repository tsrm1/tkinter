from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x350+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Виджет Radiobutton представляет переключатель, 
# который может находиться в двух состояниях: отмеченном или неотмеченном. 
# Переключатели могут создавать группу, 
# из которой одномоментно мы можем выбрать только один переключатель.

# параметры конструктора Radiobutton следующие:
# command: ссылка на функцию, которая вызывается при нажатии на переключатель
# cursor: курсор при наведении на виджет
# image: графическое изображение, отображаемое виджетом
# padding: отступы от содержимого до границы переключателя
# state: состояние виджета, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE
# text: текст виджета
# textvariable: устанавливает привязку к переменной StringVar, которая задает текст переключателя
# underline: индекс подчеркнутого символа в тексте виджета
# variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние переключателя
# value: значение переключателя
# width: ширина виджета

position = {"padx":1, "pady":1, "anchor":NW}
 
python = "Python"
java = "Java"
javascript = "JavaScript"
 
lang = StringVar(value=java)    # по умолчанию будет выбран элемент с value=java
 
header = ttk.Label(textvariable=lang)
header.pack(**position)
  
python_btn = ttk.Radiobutton(text=python, value=python, variable=lang)
python_btn.pack(**position)
  
javascript_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=lang)
javascript_btn.pack(**position)
 
java_btn = ttk.Radiobutton(text=java, value=java, variable=lang)
java_btn.pack(**position)

###############################################################################################

# Обработка выбора пользователя
position = {"padx":6, "pady":6, "anchor":NW}
languages = ["Python", "JavaScript", "Java", "C#"]
selected_language = StringVar()    # по умолчанию ничего не выборанно
 
header = ttk.Label(text="Выберите язык")
header.pack(**position)
 
def select():
    header.config(text=f"Выбран {selected_language.get()}")
 
for lang in languages:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)
    lang_btn.pack(**position)














###############################################################################################
root.mainloop()
