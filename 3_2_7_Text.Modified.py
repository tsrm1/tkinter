from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# # События
# # Для виджета Text определено событие <<Modified>>, 
# # которое срабатывает при изменении текста в текстовом поле. 
# # Однако оно срабатывает один раз. 
# # И в этом случае мы можем обработать стандартные события клавиатуры. 
# # Например, событие освобождения клавиши <KeyRelease>:


# def on_modified(event):
#     label["text"]=editor.get("1.0", END)
 
# editor = Text(height=8)
# editor.pack(fill=X)
# editor.bind("<KeyRelease>", on_modified)
 
# label = ttk.Label()
# label.pack(anchor=NW)

###############################################################################################

# динамическое получение выделенного текста. 
# В этом случае мы можем обработать событие <<Selection>>. 
# Например, при выделении текста выведем выделенный фрагмент в метку Label:

def on_modified(event):
    label["text"]=editor.selection_get()
 
editor = Text(height=8)
editor.pack(fill=X)
editor.bind("<<Selection>>", on_modified)
 
label = ttk.Label()
label.pack(anchor=NW)




###############################################################################################
root.mainloop()
