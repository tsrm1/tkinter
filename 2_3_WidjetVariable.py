from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################


# Привязка виджетов к переменным
# StringVar()
# IntVar()
# BooleanVar()
# DoubleVar()

# Типы имеют параметр value, который позволяет установить значение по умолчанию. 

# Типы имеют имеют два метода:
# set(value): устанавливает значение, которое передано через параметр
# get(): возвращает значение

###############################################################################################
message = StringVar()
 
label = ttk.Label(textvariable=message)
label.place(x=5, y=5)
 
entry = ttk.Entry(textvariable=message)
entry.place(x=5, y=25)
 
button = ttk.Button(textvariable=message)
button.place(x=5, y=50)
###############################################################################################

def click_button():
    value = clicks.get()    # получаем значение
    clicks.set(value + 1)   # устанавливаем новое значение
 
 
clicks = IntVar(value=0)    # значение по умолчанию
 
btn = ttk.Button(textvariable=clicks, command=click_button)
btn.place(x=5, y=85)

###############################################################################################

# Отслеживание изменения переменной
# Класс StringVar позволяет отслеживать чтение и изменение своего значения. 
# Для отслеживания у объекта StringVar вызывается метод trace_add()
# trace_add(trace_mode, function)

# Первый параметр представляет отслеживаемое событие и может принимать следующие значения:
# write: изменение значения
# read: чтение значения
# unset: удаление значения
# Также можно передать список из этих значений, 
# если нам надо отслеживать несколько событий.

# Второй параметр представляет функцию, 
# которая будет вызываться при возникновении события из первого параметра. 
# Эта функция должна принимать один параметр.

def check(*args):
    print(name)
    if name.get()=="admin":
        result.set("запрещенное имя")
    else: 
        result.set("норм")



name = StringVar()
result = StringVar()
 
name_entry = ttk.Entry(textvariable=name) 
name_entry.place(x=5, y=125)
 
check_label = ttk.Label(textvariable=result)
check_label.place(x=5, y=150)
 
# отслеживаем изменение значения переменной name
name.trace_add("write", check)





###############################################################################################
root.mainloop()
