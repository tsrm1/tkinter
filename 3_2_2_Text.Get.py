from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# Получение текста
# Для получения введенного текста применяется метод get():
# get(start, end)
# Параметр start указывает на начальный символ, 
# а end - на конечный символ, текст между которыми надо получить. 
# Оба параметра в формате "line.colunm", 
# где line - номер строки, а "column" - номер символа. 
# Для указания последнего символа применяется константа END:


editor = Text(height=5)
editor.pack(anchor=N, fill=X)
 
label=ttk.Label()
label.pack(anchor=N, fill=BOTH)
 
def get_text():
    label["text"] = editor.get("1.0", "end")
 
button = ttk.Button(text="Click", command=get_text)
button.pack(side=BOTTOM)


###############################################################################################
root.mainloop()

