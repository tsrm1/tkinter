from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# Удаление текста
# Для удаления текста применяется метод delete()
# delete(start, end)

editor = Text(height=10)
editor.pack(anchor=N, fill=BOTH)
 
 
def delete_text():
    editor.delete("1.0", END)
 
button = ttk.Button(text="Clear", command=delete_text)
button.pack(side=BOTTOM)


###############################################################################################
root.mainloop()

