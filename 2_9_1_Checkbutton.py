from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

from tkinter.messagebox import showinfo     # для отображения сообщений
# Checkbutton
# Элемент Checkbutton представляет собой флажок, который может находиться в двух состояниях: отмеченном и неотмеченном.
# Конструктор Checkbutton принимает ряд параметров, отметим основные из них:
# command: ссылка на функцию, которая вызывается при нажатии на флажок
# cursor: курсор при наведении на элемент
# image: графическое изображение, отображаемое на элементе
# offvalue: значение флажка в неотмеченном состоянии, по умолчанию равно 0
# onvalue: значение флажка в отмеченном состоянии, по умолчанию равно 1
# padding: отступы от текста до границы флажка
# state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE
# text: текст элемента
# textvariable: привязанный к тексту объект StringVar
# underline: индекс подчеркнутого символа в тексте флажка
# variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние флажка
# width: ширина элемента


enabled = IntVar()
  
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)
enabled_checkbutton.place(x=5, y=5)
  
enabled_label = ttk.Label(textvariable=enabled)
enabled_label.place(x=5, y=25)

###############################################################################################

# Обработка изменения флажка

# Здесь при изменении состояния флажка срабатывает функция checkbutton_changed. 
# В ней в зависимости от состояния флажка 
# (а точнее в зависимости от значения переменной enabled) 
# с помощью встроенной функции showinfo() 
# отображаем сообщение о состоянии флажка
def checkbutton_changed():
    if enabled.get() == 1:          # флаг = 1 (включен)
        showinfo(title="Info", message="Включено")
    else:                           # флаг = 2 (выключен)
        showinfo(title="Info", message="Отключено")
 
enabled = IntVar()
  
enabled_checkbutton = ttk.Checkbutton(text="Info", variable=enabled, command=checkbutton_changed)
enabled_checkbutton.place(x=5, y=55)

###############################################################################################

# onvalue и offvalue
# Параметры onvalue и offvalue позволяют задать значение флажка 
# в отмеченном и неотмеченном состоянии. 
# По умолчанию они равны 1 и 0 соответственно

def checkbutton_changed():
    showinfo(title="Info", message=status.get())
 
status = StringVar()
  
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=status, offvalue="Откл.", onvalue="Вкл.", command=checkbutton_changed)
enabled_checkbutton.place(x=5, y=80)

###############################################################################################

# Текст флажка
enabled_on = "Включено"
enabled_off = "Отключено"
enabled = StringVar(value=enabled_on)
  
enabled_checkbutton = ttk.Checkbutton(textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)
enabled_checkbutton.place(x=5, y=110)





###############################################################################################
root.mainloop()
