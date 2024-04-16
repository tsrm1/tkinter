from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x350+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Установка стилей
label = ttk.Label(text="Hello World")
label.pack(anchor=CENTER, expand=1)
print(label["style"])

# Если к виджету применяется стиль по умолчанию,
# то название стиля можно получить с помощью метода winfo_class():
print(label.winfo_class())      # => TLabel


###############################################################################################
# Определение и применение стилей
# Стиль в Tkinter представляет объект Style. 
# У данного объект есть метод configure(), 
# который позволяет настроить стиль

label_style = ttk.Style()
label_style.configure("My.TLabel",          # имя стиля
                    font="helvetica 14",    # шрифт
                    foreground="#004D40",   # цвет текста
                    padding=10,             # отступы
                    background="#B2DFDB")   # фоновый цвет
 
label = ttk.Label(text="Hello World", style="My.TLabel")
label.pack(anchor=CENTER, expand=1)



###############################################################################################
# Имена стилей
# Имя создаваемых стилей имеют следующий формат:
# новый_стиль.встроенный_стиль

# Расширение встроенных стилей
# Вместо создания новых стилей можно просто изменить отдельные характеристики 
# уже существующих:

ttk.Style().configure("TLabel",  font="helvetica 13", foreground="#000088", padding=8, background="#cccccc") 
 
ttk.Label(text="Hello World!").pack(anchor=NW, padx=6, pady=6)
ttk.Label(text="Bye World..").pack(anchor=NW, padx=6, pady=6)


###############################################################################################

# Применение стиля ко всем виджетам
# Выше стиль применялся к меткам Label, к другим же типам виджетов он не применялся. 
# Если же мы хотим, чтобы у нас был бы общий стиль для всех типов виджетов, 
# то в метод configure() в качестве имени стиля передается "."

ttk.Style().configure(".",  font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB") 
 
ttk.Label(text="Hello World!").pack(anchor=NW, padx=6, pady=6)
ttk.Button(text="Click").pack(anchor=NW, padx=6, pady=6)

###############################################################################################
root.mainloop()