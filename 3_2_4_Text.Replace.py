from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# Замена текста
# Для замены текста применяется метод replace():
# replace(start, end, chars)

# Параметр start указывает на начальный символ, 
# а end - на конечный символ, текст между которыми надо заменить. 
# Оба параметра в формате "line.colunm", где line - номер строки, 
# а "column" - номер символа. Для указания последнего символа применяется константа END. 
# Последний параметр - chars - строка, на которую надо заменить. 
# Например, замена первых четырех символов на строку "дама":

editor = Text(height=10)
editor.pack(anchor=N, fill=BOTH)
editor.insert("1.0", "мама мыла раму")
 
 
def edit_text():
    editor.replace("1.0", "1.4", "ДАМА")
 
button = ttk.Button(text="Replace", command=edit_text)
button.pack(side=BOTTOM)

###############################################################################################
root.mainloop()
