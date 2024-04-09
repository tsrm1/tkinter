from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Установка родительского контейнера. Frame
# Frame отображает прямоугольник и обычно применяется для организации интерфейса в отдельные блоки. Некоторые основные параметры, которые мы можем установить через конструктор класса Frame:
# borderwidth: толщина границы фрейма, по умолчанию равно 0
# relief: определяет тип границы, может принимать значения SUNKEN, RAISED, GROOVE, RIDGE
# cursor: устанавливает курсор при наведении на фрейм
# height: высота фрейма
# width: ширина фрейма
# padding: отступы от вложенного содержимого до границ фрейма
# padding=10              # устанавливает общий доступ в 10 единиц
# padding=[8, 10]         # отступ по горизонтали - 8, отступ по вертикали - 10
# padding=[8, 10, 6, 5]   # отступ слева 8, сверху - 10, справа - 6 и снизу 5

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Введите имя")
name_label.pack(anchor=NW)
 
name_entry = ttk.Entry(frame)
name_entry.pack(anchor=NW)
 
frame.pack(anchor=NW, fill=X, padx=5, pady=5)
###############################################################################################

def create_frame(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    # добавляем на фрейм метку
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    # добавляем на фрейм текстовое поле
    entry = ttk.Entry(frame)   
    entry.pack(anchor=NW)
    # возвращаем фрейм из функции
    return frame


name_frame = create_frame("Введите имя")
name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
 
email_frame = create_frame("Введите email")
email_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
 

###############################################################################################
root.mainloop()
