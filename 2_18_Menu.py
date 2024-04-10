from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
from tkinter import messagebox              # подключаем пакет Окно сообщений

root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Меню
# Для создания иерархического меню в tkinter применяется виджет Menu. 
# Основные параметры Menu:
# activebackground: цвет активного пункта меню
# activeborderwidth: толщина границы активного пункта меню
# activeforeground: цвет текста активного пункта меню
# background / bg: фоновый цвет
# bd: толщина границы
# cursor: курсор указателя мыши при наведении на меню
# disabledforeground: цвет, когда меню находится в состоянии DISABLED
# font: шрифт текста
# foreground / fg: цвет текста
# tearoff: меню может быть отсоединено от графического окна. В частности, при создании подменю а скриншоте можно увидеть прерывающуюся линию в верху подменю, за которую его можно отсоединить. Однако при значении tearoff=0 подменю не сможет быть отсоединено.
 
# доступны следующие методы:
# add_command(options): добавляет элемент меню через параметр options
# add_cascade(options): добавляет элемент меню, который в свою очередь может представлять подменю
# add_separator(): добавляет линию-разграничитель
# add_radiobutton(options): добавляет в меню переключатель
# add_checkbutton(options): добавляет в меню флажок


def help_click():
    messagebox.showinfo("GUI Python", "Нажата опция Help")

def exit_click():
    root.destroy()


root.option_add("*tearOff", FALSE)      # чтобы избавиться от пунктирной линии в подменю
main_menu = Menu()
file_menu = Menu()
# file_menu = Menu(tearoff=0)             # tearoff=0, чтобы избавиться от пунктирной линии в подменю
save_menu = Menu()

save_menu.add_command(label="Save")
save_menu.add_command(label="Save as ...")
save_menu.add_command(label="Export to ...")
save_menu.add_command(label="Convert to ...")

file_menu.add_command(label="New")
file_menu.add_cascade(label="Save", menu=save_menu)
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_click)



main_menu.add_cascade(label="File", menu=file_menu)     # добавляет элемент меню, который в свою очередь может представлять подменю
main_menu.add_command(label="Edit")     # добавляет элемент меню, который в свою очередь может представлять подменю
main_menu.add_cascade(label="View")     # добавляет элемент меню, который в свою очередь может представлять подменю
main_menu.add_command(label="Help", command=help_click)     # добавляет элемент меню, который в свою очередь может представлять подменю
 
root.config(menu=main_menu)             # установить Menu для текущего окна




###############################################################################################
root.mainloop()
