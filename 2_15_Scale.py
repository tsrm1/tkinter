from tkinter import *
from tkinter import ttk                     # подключаем пакет ttk, улучшенные виджеты
 
root = Tk()                                 # Инициалиция окна
root.title("Main window")                   # название окна
root.iconbitmap(default="ico/favicon.ico")  # установка иконки для окна
root.geometry("300x250+400+200")            # "Ширина x Высота + Смещение по X + Смещение по Y"
root.minsize(200,150)                       # минимальные размеры: ширина - 200, высота - 150
###############################################################################################

# Scale представляет ползунок со шкалой, на которой можно выбрать одно из числовых значений.
# Среди параметров Scale следует отметить следующие:
# orient: направление виджета. 
# Может принимать значения HORIZONTAL/"horizontal" и VERTICAL/"vertical"
# from_: начальное значение шкалы виджета, представляет тип float
# to: конечное значение шкалы виджета, представляет тип float
# length: длина виджета
# command: функция, которая выполняется при изменении текущего значения
# value: текущее значение шкалы виджета, представляет тип float
# variable: переменная IntVar или DoubleVar, к которой привязано текущее значение виджета

verticalScale = ttk.Scale(orient=VERTICAL, length=100, from_=0.0, to=100.0, value=50)
verticalScale.pack()
 
horizontalScale = ttk.Scale(orient=HORIZONTAL, length=100, from_=0.0, to=100.0, value=30)
horizontalScale.pack()
###############################################################################################

# Привязка к переменной
val = IntVar(value=10)
 
ttk.Label(textvariable=val).pack(anchor=NW)
 
horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=0.0, to=100.0, variable=val)
horizontalScale.pack(anchor=NW)
###############################################################################################

# Обработка изменения значения
# Параметр command позволяет установить функцию, 
# которая будет выполняться при изменении текущего значения Scale. 
# В качестве параметра в эту функцию передается новое значение:

def get_scale_float(newVal):        # чтобы получить значение scale типа float
    label["text"] = newVal
    # или так
    # label["text"] = scale.get()     # получить значение типа float в строковом виде

def get_scale_int(newVal):          # чтобы получить значение scale типа int
    float_value = float(newVal)     # получаем из строки значение float
    int_value = round(float_value)  # округляем до целочисленного значения
    label["text"] = int_value


label = ttk.Label()
label.pack(anchor=NW)
 
scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=0.0, to=100.0, command=get_scale_int)
scale.pack(anchor=NW)

###############################################################################################
root.mainloop()
